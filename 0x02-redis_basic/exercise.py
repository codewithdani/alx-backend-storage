#!/usr/bin/env python3
""" Cache class in Python using the redis library: """
from uuid import uuid4
import redis
from typing import Union


class Cache:
    """ declares a Cache redis class """
    def __init__(self):
        """ Create an instance of the Redis client """
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generate a random key using uuid """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
