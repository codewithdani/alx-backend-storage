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
    def wrapper(url: str, *args, **kwargs) -> str:
        """ Generate keys for count and cache """
        count_key = f"count:{url}"
        cache_key = f"cache:{url}"

        """ Increment the count for the URL """
        redis_client.incr(count_key)

        """ Check if the result is already cached """
        cached_result = redis_client.get(cache_key)
        if cached_result:
            return cached_result.decode('utf-8')

        """ Call the original method to get the result """
        result = method(url, *args, **kwargs)

        """ Cache the result with an expiration time of 10 seconds """
        redis_client.setex(cache_key, 10, result)

        return result

    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """ Returns HTML content of a url """
    res = requests.get(url)
    return res.text
