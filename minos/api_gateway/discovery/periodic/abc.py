# Copyright (C) 2020 Clariteia SL
#
# This file is part of minos framework.
#
# Minos framework can not be copied and/or distributed without the express
# permission of Clariteia SL.

from abc import (
    ABC,
)

from minos.api_gateway.common import (
    ClientHttp,
    MinosConfig,
)
from minos.api_gateway.discovery.database import (
    MinosRedisClient,
)


class HealthStatusCheck(ABC):
    def __init__(self, config: MinosConfig):
        self.redis_cli = MinosRedisClient(config=config)
        self.redis_conn = self.redis_cli.get_redis_connection()
        self._client_http = ClientHttp()

    async def perform_health_check(self):
        status_code = None
        for key in self.redis_conn.scan_iter():
            try:
                data = self.redis_cli.get_data(key)
                try:
                    status_code = await self.__request(data)
                finally:
                    self.__update(status_code, key, data)
            finally:
                pass

        return True

    async def __request(self, data):
        status_code = None
        if len(data) > 0 and "ip" in data and "name" in data:
            url = "http://{0}/system/health".format(data["ip"])
            if "port" in data:
                if data["port"] is not None:
                    url = "http://{0}:{1}/system/health".format(data["ip"], data["port"])

            try:
                async with ClientHttp() as client:
                    response = await client.get(url=url)

                status_code = response.status
            except Exception:
                print("Error connecting to {0}".format(url))

        return status_code

    def __update(self, status_code, key, data):
        try:
            # If response status code == 200
            # set status to True else,
            # set status to False
            perform_update = False
            if status_code == 200:
                if data["status"] is not True:
                    data["status"] = True
                    perform_update = True
            else:
                if data["status"] is not False:
                    data["status"] = False
                    perform_update = True

            if perform_update:
                self.redis_cli.set_data(key, data)

        finally:
            pass
