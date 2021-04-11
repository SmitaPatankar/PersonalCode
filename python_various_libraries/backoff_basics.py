# decorator for functions to get retried until condition is met
# Decorator support both regular functions for synchronous code and asyncio’s coroutines for asynchronous code.
import backoff
import requests


# can pass tuple also
@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=3)
def get_url(url):
    print("here")
    return requests.get(url)


get_url("http://test")


# @backoff.on_predicate(backoff.fibo, lambda x: x == [], max_value=13)
# def poll_for_messages(queue):
#     return queue.get()
