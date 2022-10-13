import json
import time
import random
import hashlib

from os import makedirs
from os.path import exists


def hash_string_sha224(data):
    return hashlib.sha224(data.encode()).hexdigest()


def get_timestamp():
    return int(time.time())


def encode(data):
    return data.encode()


def decode(data):
    return data.decode()


def deserialize(data):
    return json.loads(data)


def serialize(data):
    return json.dumps(data)


async def isff(path_ff):  # is folder-file
    return exists(path_ff)


async def create_folder(path_folder):
    if not await isff(path_folder):
        makedirs(path_folder)


if __name__ == '__main__':
    # print(hash_string_sha224('Hello World'))
    # print(isff('./utils.py'))
    pass
