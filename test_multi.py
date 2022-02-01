import time
from threading import Thread

def func_wait(n: int, run_type: str) -> None:
    """
    Wait n seconds
    Args:
        n:  seconds
        id: type of run
    Reterns:
        None
    """
    print(f"--> start {run_type}")
    print(f"--> wait {run_type} {n}s")
    time.sleep(n)
    print(f"--> end {run_type}")

if __name__ == "__main__":
    n = 5

    # singel
    start = time.time()
    func_wait(n, "single")
    end = time.time()
    print(f"--> single: {round(end - start, 2)}")

    # thread
    threads = []
    for i in range(n):
        threads.append(Thread(target=func_wait, args=(n/5, f"thread-{i}")))
    start = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end = time.time()
    print(f"--> thread: {round(end - start, 2)}")

