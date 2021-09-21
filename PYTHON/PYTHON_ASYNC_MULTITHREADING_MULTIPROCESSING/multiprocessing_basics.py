# switches between cores that are not busy
# args need to be pickled so they can be reconstructed in other script


import time
import multiprocessing


def m(sec):
    print(f"start {sec}")
    time.sleep(sec)
    print(f"end {sec}")


if __name__ == '__main__':
    start = time.perf_counter()

    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=m, args=(1.5,))
        p.start()
    for p in processes:
        p.join()

    end = time.perf_counter()
    print(end-start)
