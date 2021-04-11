# switches between cores that are not busy
# args need to be pickled so they can be reconstructed in other script


import time
import concurrent.futures


def m(sec):
    print(f"start {sec}")
    time.sleep(sec)
    return f"end {sec}"


if __name__ == '__main__':
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        # futures = [executor.submit(m, sec) for sec in secs]
        # for f in concurrent.futures.as_completed(futures):
        #     print(f.result())
        results = executor.map(m, secs)
        for result in results:
            print(result)

    end = time.perf_counter()
    print(end-start)
