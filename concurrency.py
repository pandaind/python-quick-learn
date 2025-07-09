"""
# Basics of Concurrency

# Concurrency allows multiple tasks to make progress over overlapping time periods.
# Parallelism means multiple tasks are executing at the exact same instant (e.g., on different CPU cores).
# Python offers several ways to achieve concurrency: threading, asyncio, and multiprocessing.

import threading
import time # Added for sleep examples
# import asyncio # Will be added later
# import multiprocessing # Will be added later

print("--- 1. Threading (`threading` module) ---")
# Threads run within the same process and share the same memory space.
# Good for I/O-bound tasks (tasks that spend a lot of time waiting for external operations, like network requests or file I/O).
# Python's Global Interpreter Lock (GIL) means that only one thread can hold control of the Python interpreter at any given time,
# so true parallelism for CPU-bound tasks is not achieved with threads in CPython.

print("\\n--- 1.1 Basic Threading ---")
def worker_thread_function(name, delay):
    """A simple function for a thread to execute."""
    print(f"Thread {name}: starting")
    for i in range(3):
        time.sleep(delay)
        print(f"Thread {name}: working on item {i}")
    print(f"Thread {name}: finishing")

# Original example:
# def print_numbers():
#     for i in range(5):
#         print(i)
# thread = threading.Thread(target=print_numbers)
# thread.start()
# thread.join()

# Create threads with new worker function
thread1 = threading.Thread(target=worker_thread_function, args=("Thread-A", 0.3))
thread2 = threading.Thread(target=worker_thread_function, args=("Thread-B", 0.2))

# Start threads
thread1.start()
thread2.start()

print("Main thread: All threads launched. Waiting for them to complete...")
# Wait for all threads to complete
thread1.join() # Blocks until thread1 finishes
thread2.join() # Blocks until thread2 finishes
print("Main thread: All threads finished.")


print("\\n--- 1.2 Race Conditions and Locks ---")
# When multiple threads access and modify shared data, race conditions can occur, leading to unpredictable results.
# Locks (`threading.Lock`) can be used to synchronize access to shared resources.

shared_counter = 0
counter_lock = threading.Lock() # Create a lock object

def increment_counter_unsafe():
    """Increments shared_counter without a lock (unsafe)."""
    global shared_counter
    current_val = shared_counter
    time.sleep(0.0001) # A very small delay to increase chance of race condition
    shared_counter = current_val + 1

def increment_counter_safe():
    """Increments shared_counter with a lock (thread-safe)."""
    global shared_counter
    with counter_lock: # Acquire the lock; automatically released on exit
        current_val = shared_counter
        time.sleep(0.0001)
        shared_counter = current_val + 1

NUM_THREADS_FOR_COUNTER = 50

# Unsafe increment
shared_counter = 0
threads_unsafe = []
for i in range(NUM_THREADS_FOR_COUNTER):
    t = threading.Thread(target=increment_counter_unsafe)
    threads_unsafe.append(t)
    t.start()
for t in threads_unsafe:
    t.join()
print(f"Counter value (unsafe after {NUM_THREADS_FOR_COUNTER} threads): {shared_counter}")

# Safe increment
shared_counter = 0
threads_safe = []
for i in range(NUM_THREADS_FOR_COUNTER):
    t = threading.Thread(target=increment_counter_safe)
    threads_safe.append(t)
    t.start()
for t in threads_safe:
    t.join()
print(f"Counter value (safe with lock after {NUM_THREADS_FOR_COUNTER} threads): {shared_counter}")


print("\\n--- 1.3 Daemon Threads ---")
# Daemon threads are background threads that automatically exit when the main program (all non-daemon threads) exits.
# Non-daemon threads will keep the main program running until they complete.
# By default, threads are non-daemon.

def daemon_worker():
    print("Daemon thread: starting work (will run for 0.5s)")
    time.sleep(0.5)
    print("Daemon thread: finishing (this might not print if main exits too soon and no join)")

daemon_thread_example = threading.Thread(target=daemon_worker, daemon=True)
# To see daemon behavior, you would typically not join it or ensure main program logic is short:
# daemon_thread_example.start()
# print("Main program: Daemon thread started. Main might exit before daemon prints 'finishing'.")
# time.sleep(0.1) # Give main a chance to finish quickly
print("Conceptual: A daemon thread (if started and not joined) exits when the main program exits.")


print("\\n--- 1.4 Global Interpreter Lock (GIL) ---")
# The GIL is a mutex that protects access to Python objects, preventing multiple
# threads from executing Python bytecode at the same time within a single CPython process.
print("Global Interpreter Lock (GIL) in CPython:")
print("- Allows only one thread to execute Python bytecode at a time in a single process.")
print("- Effective for I/O-bound tasks (threads can release GIL during I/O waits).")
print("- Limits true parallelism for CPU-bound tasks; use `multiprocessing` for those.")

print("\\n" + "-"*60 + "\\n") # Separator before asyncio


print("--- 2. Asynchronous Programming (`asyncio`) ---")
# `asyncio` is used for writing single-threaded concurrent code using async/await syntax.
# It's ideal for I/O-bound and high-level structured network code (e.g., many network connections).
# It uses an event loop to manage and distribute the execution of different tasks (coroutines).

import asyncio # Moved import here to group with its section

print("\\n--- 2.1 Basic asyncio with `async` and `await` ---")
async def say_after(delay, what):
    """Coroutine: A special function that can be paused and resumed."""
    await asyncio.sleep(delay)
    message = f"{what} (after {delay}s at {time.strftime('%X')})"
    print(message)
    return message

async def main_async_basic_sequential():
    """Main coroutine to run other coroutines sequentially."""
    print(f"Started main_async_basic_sequential at {time.strftime('%X')}")
    # Original example:
    # async def async_print_numbers():
    #     for i in range(5):
    #         print(i)
    #         await asyncio.sleep(1)
    # asyncio.run(async_print_numbers())
    await say_after(0.2, 'hello from basic async (1)')
    await say_after(0.1, 'world from basic async (2)')
    print(f"Finished main_async_basic_sequential at {time.strftime('%X')}")

print("Running basic asyncio tasks sequentially:")
asyncio.run(main_async_basic_sequential())

print("\\n--- 2.2 Running asyncio Tasks Concurrently ---")
# To run tasks concurrently with asyncio, you schedule them on the event loop.
# `asyncio.create_task()` schedules a coroutine to run "in the background".
# `asyncio.gather()` runs multiple awaitables (coroutines, tasks, futures) concurrently and waits for all to complete.

async def main_async_concurrent():
    print(f"Started main_async_concurrent at {time.strftime('%X')}")

    print("\\nUsing asyncio.create_task():")
    task1 = asyncio.create_task(say_after(0.3, 'hello from create_task'))
    task2 = asyncio.create_task(say_after(0.1, 'world from create_task'))
    print("Tasks created and scheduled via create_task().")
    # Wait for tasks to complete (tasks run concurrently before these awaits)
    await task1
    await task2
    print("Finished create_task() section.")

    print("\\nUsing asyncio.gather():")
    results = await asyncio.gather(
        say_after(0.3, 'task A from gather'),
        say_after(0.1, 'task B from gather'),
        say_after(0.2, 'task C from gather')
    )
    print(f"Results from gather: {results}")
    print(f"Finished main_async_concurrent at {time.strftime('%X')}")

print("\\nRunning asyncio tasks concurrently (output order of tasks may vary):")
asyncio.run(main_async_concurrent())


print("\\n" + "-"*60 + "\\n")
print("--- 3. Multiprocessing (`multiprocessing` module) ---")
# `multiprocessing` enables true parallelism by creating separate processes, each with its own
# Python interpreter and memory space. This bypasses the GIL, making it suitable for CPU-bound tasks.
import multiprocessing # Moved import here
import os # For os.getpid()

def cpu_bound_worker_mp(number):
    """A simple CPU-bound task for multiprocessing."""
    process_name = multiprocessing.current_process().name
    print(f"Process (PID {os.getpid()}), Name {process_name}: calculating sum up to {number}")
    total_sum = sum(i for i in range(number))
    print(f"Process (PID {os.getpid()}), Name {process_name}: sum for {number} = {total_sum}")
    return total_sum

# Guard for multiprocessing code:
if __name__ == '__main__':
    # This check is crucial on platforms like Windows where child processes re-import the main module.
    # It ensures that the code to create new processes is only run when the script is executed directly.

    print("\\n--- 3.1 Basic Multiprocessing with `Process` ---")
    numbers_to_process_mp = [10**5, 10**5 + 100] # Reduced size for faster example
    processes_mp = []
    print("MainProcess: Launching worker processes...")
    for i, num in enumerate(numbers_to_process_mp):
        process = multiprocessing.Process(target=cpu_bound_worker_mp, args=(num,), name=f"WorkerProcMP-{i}")
        processes_mp.append(process)
        process.start()

    print("MainProcess: All worker processes launched. Waiting for them to complete...")
    for process in processes_mp:
        process.join()
    print("MainProcess: All worker processes finished.")


    print("\\n--- 3.2 Using a `Pool` of Workers for Parallel Map ---")
    from multiprocessing import Pool # Pool can be imported here

    def square_number_mp(n):
        # print(f"Process (PID {os.getpid()}) squaring {n}") # Can be verbose
        time.sleep(0.05) # Simulate some work
        return n * n

    numbers_for_pool = list(range(1, 9)) # [1, 2, ..., 8]
    print(f"Squaring numbers using a Pool: {numbers_for_pool}")

    # Using 'with' statement ensures the pool is properly closed.
    # If no argument to Pool(), it defaults to os.cpu_count() processes.
    # Limit pool size for example to prevent too many processes on shared test runners.
    num_processes_for_pool = min(4, os.cpu_count() if os.cpu_count() else 1)
    with Pool(processes=num_processes_for_pool) as pool:
        squared_results = pool.map(square_number_mp, numbers_for_pool)
    print(f"Squared results from Pool.map: {squared_results}")
    print("`multiprocessing.Pool` is excellent for parallelizing map-style operations on data.")

else:
    # This message will be printed if this script is imported as a module
    print("\\nMultiprocessing examples (Process, Pool) are inside `if __name__ == '__main__':` block.")
    print("To see them run, execute this script directly.")


print("\\n" + "-"*60 + "\\n")
# Interview Tip:
# - Understand the difference between Concurrency and Parallelism.
# - Threading: Good for I/O-bound tasks, GIL limitations for CPU-bound tasks in CPython.
#   Know about race conditions and how to use Locks (`threading.Lock`). Daemon threads.
# - Asyncio: Single-threaded concurrency using an event loop, `async/await`. Ideal for high-throughput I/O.
#   Understand how to run tasks concurrently (e.g., `asyncio.gather`, `asyncio.create_task`).
# - Multiprocessing: True parallelism for CPU-bound tasks by using multiple processes, bypassing GIL.
#   Be aware of the `if __name__ == '__main__':` guard for cross-platform compatibility and structure.
#   Know about `Process` and `Pool`.
# - Choose the right tool for the job based on task type (I/O-bound vs. CPU-bound) and complexity.

# Common Interview Question:
# Q: How can you create a simple thread in Python?
# A: Use the `threading.Thread` class, providing a `target` function and optional `args`.
#    Call the `start()` method on the thread object to begin its execution, and `join()`
#    to wait for it to complete if needed.
#    Example:
#    `import threading, time`
#    `def my_func(): print("Thread running"); time.sleep(0.1)`
#    `t = threading.Thread(target=my_func)`
#    `t.start()`
#    `t.join()`
#
# Q: What is the GIL and how does it affect Python concurrency?
# A: The Global Interpreter Lock (GIL) is a mutex in CPython that allows only one thread
#    to hold control of the Python interpreter at any given time. This means that even on
#    multi-core processors, only one thread can execute Python bytecode at once.
#    - For I/O-bound operations (like network requests, file reading/writing), threads can
#      release the GIL while waiting, allowing other threads to run, thus achieving concurrency.
#    - For CPU-bound operations (like complex calculations purely in Python), the GIL becomes a
#      bottleneck, preventing true parallelism with threads. For such tasks, `multiprocessing`
#      is preferred as each process gets its own interpreter and memory space, bypassing the GIL.
#
# Q: When would you use `threading` vs. `asyncio` vs. `multiprocessing`?
# A: - `threading`: For I/O-bound tasks where operations spend time waiting (e.g., network calls,
#      file system operations) and you want simpler shared-memory model (with careful locking).
#    - `asyncio`: For a large number of I/O-bound tasks (e.g., thousands of network connections)
#      within a single thread, using an event loop. It can be more efficient than threading for
#      such high-concurrency I/O scenarios due to lower overhead per task.
#    - `multiprocessing`: For CPU-bound tasks that require significant computation and can benefit
#      from true parallelism across multiple CPU cores, as it bypasses the GIL.
"""