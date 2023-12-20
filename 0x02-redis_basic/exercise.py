#!/usr/bin/env python3
""" Cache class in Python using the redis library: """
from uuid import uuid4
import redis
from typing import Union, Callable


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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ Get the data from Redis """
        data = self._redis.get(key)
        if fn:
            data = fn(value)
        return data

    def get_str(self, key: str) -> str:
        """ Convenience method for getting a string """
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ Convenience method for getting an integer """
        data = self._redis.get(key)
        try:
            data = int(value.decode("utf-8"))
        except Exception:
            data = 0
        return data
