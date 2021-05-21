# Copyright (C) 2020 Clariteia SL
#
# This file is part of minos framework.
#
# Minos framework can not be copied and/or distributed without the express
# permission of Clariteia SL.

"""API Router is responsible for obtaining the connection values for each domain name.

This module obtains the IP, port and status of a microservice. Using the domain name,
it performs a Redis lookup by key value. The value is stored in Redis as JSON.

    Typical usage example:

        class OrdersMinosApiRouter(MinosApiRouter):
            pass

        foo = OrdersMinosApiRouter('order')
        bar = foo.conn_values()
"""

import json
from abc import (
    ABC,
)

import redis

from minos.api_gateway.common import (
    MinosConfig,
)


class MinosRedisClient(ABC):
    """Class that connects to Redis and returns the configuration values according to domain name.

    The connection to Redis is made via the environment variables: REDIS_HOST, REDIS_PORT, REDIS_PASSWORD.

    Attributes:
        domain: A string which specifies the Domain Name. Example: order, cart, customer ....
    """

    __slots__ = "_redis_host", "_redis_port", "_redis_password", "redis"

    def __init__(self, config: MinosConfig):
        """Perform initial configuration and connection to Redis"""

        self._redis_host = config.discovery.database.host
        self._redis_port = config.discovery.database.port
        self._redis_password = config.discovery.database.password

        self.redis = self.__redis_connect()

    def __redis_connect(self):
        """Perform connection to Redis"""

        try:
            redis_connection = redis.Redis(host=self._redis_host, port=self._redis_port, password=self._redis_password)
            redis_connection.ping()
        except Exception:
            raise Exception

        return redis_connection

    def get_data(self, key: str) -> str:
        """Get redis value by key"""
        json_data = {}
        try:
            redis_data = self.redis.get(key)
            json_data = json.loads(redis_data)

        except Exception:
            pass

        return json_data

    def set_data(self, key: str, data: dict):
        flag = True
        try:
            self.redis.set(key, json.dumps(data))
        except Exception:  # pragma: no cover
            flag = False

        return flag

    def update_data(self):  # pragma: no cover
        """Update specific value"""
        pass

    def delete_data(self, key: str):
        deleted_elements = self.redis.delete(key)

        if deleted_elements > 0:
            return True
        else:
            return False

    def get_redis_connection(self):
        """Redis connection itself"""
        return self.redis

    def flush_db(self):
        self.redis.flushdb()
