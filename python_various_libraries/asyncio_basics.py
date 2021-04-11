# Problem program
"""
def find_divisibles(inrange, div_by):
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
    return located


def main():
    divs1 = find_divisibles(508000, 34113)  # will hang here and wont give other results
    divs2 = find_divisibles(100052, 3210)
    divs3 = find_divisibles(500, 3)


if __name__ == "__main__":
    main()
"""

# Solution program with asyncio
# async io
# for asynchronous programming
# aware of tasks in parallel, but not doing them in parallel
# tie shoe in between jog  - concurrently
# everything on page loads except a slower image because that server is not responding/down
# aiohttp for http tasks asynchronously
# threading or processing adds lot of things that we may not be interested in
# needs a event loop and need to give it tasks
# main coroutine needs to run until its done

import asyncio


async def find_divisibles(inrange, div_by):
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 50000 == 0:
            await asyncio.sleep(0.00001)  # simulation of i/o
    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
    return located


async def main():
    divs1 = loop.create_task(find_divisibles(50800000, 34113))  # will hang here and wont give other results, hence need async
    divs2 = loop.create_task(find_divisibles(500, 3))
    divs3 = loop.create_task(find_divisibles(100052, 3210))
    await asyncio.wait([divs1, divs2, divs3])  # else they'll just be gone
    return divs1, divs2, divs3

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()  # initialize loop
        # loop.set_debug(1)
        d1, d2, d3 = loop.run_until_complete(main())
        print(d1.result())
        print(d2.result())
        print(d3.result())
    except Exception as e:
        pass
    finally:
        loop.close()
