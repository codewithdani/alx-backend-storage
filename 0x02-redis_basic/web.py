#!/usr/bin/env python3
"""
Module for web-related functions.
"""

import redis
import requests
from functools import wraps
from typing import Callable

# Initialize Redis client
store = redis.Redis()
"""The module-level Redis instance."""


def cache_with_count(method: Callable) -> Callable:
    """
    Decorator to cache the output of fetched data and
    track the number of accesses.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper function for caching the output and tracking accesses.
        """
        store.incr(f'count:{url}')
        result = store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        store.setex(f'result:{url}', 10, result)
        return result

    return wrapper


@cache_with_count
def get_page(url: str) -> str:
    """
    Returns the HTML content of a URL, caches the response,
    and tracks accesses.
    """
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    # Example usage:
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.com"
    page_content = get_page(url)
    print(page_content)

    # Retrieve and print the access count for the URL
    count_key = f"count:{url}"
    access_count = store.get(count_key)
    print(f"Access count for {url}: {int(access_count)}")
