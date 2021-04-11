# http client just like requests
# for downloading web pages or interacting with APIs

import httpx
r = httpx.get("https://www.example.org")
print(r.status_code)
print(r.text)

# new functionality
# async capable http client - concurrency model is less resource intensive
# supports http/1.1 and http/2
# can make requests directly to wsgi or flask apps
# type annotated
# strict timeouts - 5sec by default
# http2 is binary not textual, helps in compression
# multiple requests and responses across same connection in http2  - lower latency
# mocking

import httpx
import trio
async def main():
    # can take http2=True
    async with httpx.AsyncClient() as client:
        response = await client.get("https://www.example.org")
        print(response)
trio.run(main)
