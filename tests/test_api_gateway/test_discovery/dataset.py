import random
import socket
import struct
from uuid import uuid4


def generate_random_microservice_names(quantity: int):
    random_names = [f"test_endpoint_{str(uuid4())}" for x in range(quantity)]

    return random_names


def generate_record(name):
    ip = socket.inet_ntoa(struct.pack(">I", random.randint(1, 0xFFFFFFFF)))
    port = random.randint(1, 9999)

    record = {
        "address": f"{ip}",
        "port": port,
        "endpoints": [["GET", f"test_endpoint_{name}"], ["POST", f"test_endpoint_{name}"]],
    }

    return record


def generate_record_old(x):
    ip = socket.inet_ntoa(struct.pack(">I", random.randint(1, 0xFFFFFFFF)))
    port = random.randint(1, 9999)
    name = f"microservice_{x}"

    record = {
        "address": f"{ip}",
        "port": port,
        "endpoints": [["GET", f"test_endpoint_{name}"], ["POST", f"test_endpoint_{name}"]],
    }

    return name, record
