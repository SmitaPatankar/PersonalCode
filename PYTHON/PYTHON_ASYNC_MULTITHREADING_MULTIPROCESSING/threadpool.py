import time
import concurrent.futures


start = time.perf_counter()


def m(sec):
    print(f"start {sec}")
    time.sleep(sec)
    return f"end {sec}"


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]

    # futures = [executor.submit(m, sec) for sec in secs]
    # for f in concurrent.futures.as_completed(futures):
    #     print(f.result())

    results = executor.map(m, secs)
    for result in results:
        print(result)

end = time.perf_counter()
print(end-start)
