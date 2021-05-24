import time
import threading

start = time.perf_counter()


def m(sec):
    print(f"sleeping for {sec} secs")
    time.sleep(sec)
    print("end")


threads = []
for _ in range(10):
    t = threading.Thread(target=m, args=[1.5])
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()  # to wait before executing rest of the code in main program
end = time.perf_counter()
print(end-start)
