import contextlib
import os
import time


def m():
    for i in range(1,5):
        yield str(i)


@contextlib.contextmanager
def write_temp_file(name, iterable, directory='/tmp'):
    report_path = os.path.join(directory, name)
    with open(report_path, 'w') as f:
        for i in iterable:
            f.write(i)
    try:
        yield report_path
    finally:
        os.remove(report_path)


with write_temp_file("temp1.txt", m()) as first_results:
    with write_temp_file("temp2.txt", m()) as second_results:
        # do something like zip them to a permanent location
        time.sleep(10)

# during execution, /tmp has temp1.txt ad temp2.txt
# later its gone
