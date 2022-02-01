import time
from threading import Thread
from multiprocessing import Pool
# idea: https://www.youtube.com/watch?v=7Nh5DhWKLoQ

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
    for i in range(n):
        tmp = 2**1e3
    time.sleep(n)
    print(f"--> end {run_type}")


if __name__ == "__main__":
    n_wait = 5
    n_split = 5

    # singel
    print(f"\nSINGLE START")
    start = time.time()
    func_wait(n_wait, "single")
    end = time.time()
    print(f"SINGLE END ({round(end - start, 2)}s)")

    # threading
    print(f"\nTHREADING START")
    start = time.time()
    threads = []
    for i in range(n_wait):
        threads.append(Thread(target=func_wait, args=(int(n_wait/n_split), f"threading-{i}")))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end = time.time()
    print(f"THREADING END ({round(end - start, 2)}s)")

    # multiprocessing
    print(f"\nMUTLIPROCESSING START")
    start = time.time()
    pool = Pool(processes=n_wait)
    for i in range(n_wait):
        pool.apply_async(func=func_wait, args=(int(n_wait/n_split), f"multiprocessing-{i}"))
    pool.close()
    pool.join()
    end = time.time()
    print(f"MULTIPROCESSING END ({round(end - start, 2)}s)")
