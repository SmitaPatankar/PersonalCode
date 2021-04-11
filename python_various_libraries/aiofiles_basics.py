# handle local disk files in asyncio applications
import asyncio
import aiofiles


async def m(filename, content):
    print(f"writing {filename}")
    async with aiofiles.open(filename, mode='a') as f:
        await f.write(content)
    print(f"written {filename}")


async def main():
    s = "smita"
    a = loop.create_task(m("3.txt", s*10000))
    b = loop.create_task(m("1.txt", s*10))
    c = loop.create_task(m("2.txt", s*1000))
    await asyncio.wait([a,b,c])
    return a,b,c


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        a,b,c  = loop.run_until_complete(main())
        print(a.result())
        print(b.result())
        print(c.result())
    except Exception as e:
        print(e)
    finally:
        loop.close()

# async with aiofiles.open('filename') as f:
#     async for line in f:
#         ...
