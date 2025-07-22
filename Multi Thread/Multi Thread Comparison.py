import threading
import time
from concurrent.futures import ThreadPoolExecutor

NUM_THREADS = 1000

def dummy_task():
    time.sleep(0.01)

def run_manual_threads():
    threads = []
    start = time.time()
    for _ in range(NUM_THREADS):
        t = threading.Thread(target=dummy_task)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    end = time.time()
    print(f"Manual threading time: {end - start}")

def run_thread_pool():
    start = time.time()
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(dummy_task) for _ in range(NUM_THREADS)]
        for future in futures:
            future.result()
    end = time.time()
    print(f"ThreadPoolExecutor time: {end - start}")


print("Manual benchmark...")
run_manual_threads()

print("ThreadPool benvhmark...")
run_thread_pool()
