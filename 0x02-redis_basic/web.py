#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker """
import requests
import redis
from functools import wraps
from typing import Callable

redis_client = redis.Redis()
""" The module-level Redis instance. """


def count_url_access(method: Callable) -> Callable:
    """ Decorator counting how many times
    a URL is accessed """
    @wraps(method)
    def wrapper(url):
        """ The wrapper function for caching the output. """
        redis_client.incr(f'count:{url}')
        result = redis_client.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """ Returns HTML content of a url """
    res = requests.get(url)
    return res.text
