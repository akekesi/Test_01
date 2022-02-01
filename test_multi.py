import time
from threading import Thread
from multiprocessing import Pool
# idea: https://www.youtube.com/watch?v=7Nh5DhWKLoQ

def func_wait(n_wait: int, for_loop: list, run_type: str) -> None:
    """
    Wait n seconds
    Args:
        n_wait:     waiting time in second
        run_type:   type of run
    Reterns:
        None
    """
    print(f"--> start {run_type}")
    print(f"--> wait {run_type} {n_wait}s")
    [s, e] = for_loop
    for i in range(s, e):
        tmp = 2**i
    print(f"--> last i: {i}")
    time.sleep(n_wait)
    print(f"--> end {run_type}")


if __name__ == "__main__":
    n_wait = 5
    for_loop = 30_000
    n_split = 10

    # singel
    print(f"\nSINGLE START")
    start = time.time()
    func_wait(n_wait, [0, for_loop], "single")
    end = time.time()
    print(f"SINGLE END ({round(end - start, 2)}s)")

    # threading
    print(f"\nTHREADING START")
    start = time.time()
    threads = []
    for i in range(n_split):
        tmp = int(for_loop / n_split)
        threads.append(Thread(target=func_wait, args=(n_wait / n_split, [i * tmp, (i+1) * tmp], f"threading-{i}")))
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
    for i in range(n_split):
        tmp = int(for_loop / n_split)
        pool.apply_async(func=func_wait, args=(n_wait / n_split, [i * tmp, (i+1) * tmp], f"multiprocessing-{i}"))
    pool.close()
    pool.join()
    end = time.time()
    print(f"MULTIPROCESSING END ({round(end - start, 2)}s)")
