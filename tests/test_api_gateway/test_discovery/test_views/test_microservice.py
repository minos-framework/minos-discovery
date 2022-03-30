import asyncio

from aiohttp.test_utils import (
    AioHTTPTestCase,
    unittest_run_loop,
)

from minos.api_gateway.common import (
    MinosConfig,
)
from minos.api_gateway.discovery import (
    DiscoveryService,
)
from tests.test_api_gateway.test_discovery.dataset import (
    generate_random_microservice_names,
    generate_record,
    generate_record_old,
)
from tests.utils import (
    BASE_PATH,
)


class TestMicroserviceEndpoints(AioHTTPTestCase):
    CONFIG_FILE_PATH = BASE_PATH / "config.yml"

    async def get_application(self):
        """
        Override the get_app method to return your application.
        """
        config = MinosConfig(self.CONFIG_FILE_PATH)
        service = DiscoveryService(
            address=config.discovery.connection.host, port=config.discovery.connection.port, config=config
        )

        return await service.create_application()

    @unittest_run_loop
    async def test_post(self):
        name = "test_name"
        body = {"address": "1.1.1.1", "port": 1, "endpoints": [["GET", "test_endpoint_1"], ["POST", "test_endpoint_2"]]}

        response = await self.client.post(f"/microservices/{name}", json=body)

        self.assertEqual(201, response.status)

    async def test_bulk_update(self):
        names = generate_random_microservice_names(50)

        tasks = list()
        # Create new records
        for name in names:
            body = generate_record(name)
            tasks.append(self.client.post(f"/microservices/{name}", json=body))

        results = await asyncio.gather(*tasks)

        for result in results:
            self.assertEqual(201, result.status)

        # Update existing records
        expected = list()
        tasks = list()
        for name in names:
            body = generate_record(name)
            expected.append({"name": name, "path": f"/microservices/{name}", "body": body})
            tasks.append(self.client.post(f"/microservices/{name}", json=body))

        results = await asyncio.gather(*tasks)

        for result in results:
            self.assertEqual(201, result.status)

        # Check updated records are correct
        for record in expected:
            response = await self.client.get(
                f"/microservices?verb={record['body']['endpoints'][0][0]}&path={record['body']['endpoints'][0][1]}"
            )

            self.assertEqual(200, response.status)

            body = await response.json()

            self.assertEqual(record["body"]["address"], body["address"])
            self.assertEqual(record["body"]["port"], int(body["port"]))
            self.assertEqual(record["name"], body["name"])

    async def test_bulk_update_2(self):
        expected = list()
        tasks = list()
        # Create new records
        for x in range(50):
            name, body = generate_record_old(x)
            tasks.append(self.client.post(f"/microservices/{name}", json=body))

        results = await asyncio.gather(*tasks)

        for result in results:
            self.assertEqual(201, result.status)

        tasks = list()
        for x in range(50):
            name, body = generate_record_old(x)
            expected.append({"name": name, "path": f"/microservices/{name}", "body": body})
            tasks.append(self.client.post(f"/microservices/{name}", json=body))

        results = await asyncio.gather(*tasks)

        for result in results:
            self.assertEqual(201, result.status)

        for record in expected:
            response = await self.client.get(
                f"/microservices?verb={record['body']['endpoints'][0][0]}&path={record['body']['endpoints'][0][1]}"
            )

            self.assertEqual(200, response.status)

            body = await response.json()

            self.assertEqual(record["body"]["address"], body["address"])
            self.assertEqual(int(record["body"]["port"]), int(body["port"]))
            self.assertEqual(record["name"], body["name"])

    @unittest_run_loop
    async def test_post_missing_param(self):
        name = "test_name"
        body = {"port": 1, "endpoints": ["test_endpoint_1", "test_endpoint_2"]}

        response = await self.client.post(f"/microservices/{name}", json=body)

        self.assertEqual(400, response.status)
        self.assertIn("address", await response.text())

    @unittest_run_loop
    async def test_post_missing_name(self):
        response = await self.client.post("/microservices/")

        self.assertEqual(404, response.status)

    @unittest_run_loop
    async def test_post_empty_body(self):
        name = "test_name"

        response = await self.client.post(f"/microservices/{name}")

        self.assertEqual(400, response.status)

    @unittest_run_loop
    async def test_delete(self):
        name = "test_name"
        endpoint_name = "test_endpoint_1"
        body = {"address": "1.1.1.1", "port": 1, "endpoints": [endpoint_name]}
        await self.client.post(f"/microservices/{name}", json=body)

        response = await self.client.delete(f"/microservices/{name}")

        self.assertEqual(200, response.status)
