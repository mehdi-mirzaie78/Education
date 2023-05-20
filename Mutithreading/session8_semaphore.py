"""
    Semaphore
        Use case:   when we want to apply a limitation for shared resources and threads for ex, only 2 treads can work
        on shared resource at the same time

    BoundedSemaphore
        Use case when released more than once
"""
from threading import Semaphore, BoundedSemaphore, current_thread
from time import sleep
from utils import create_thread, start_thread, join_thread, process_timer
from typing import Callable

num = 0
lock = Semaphore(value=2)       # value is the number of threads that have access to shared resources
# lock = BoundedSemaphore(value=2)
"""
when we release twice there's going to be extra space for other threads so it makes sense to use BoundedSemaphore
"""


def add():
    global num
    lock.acquire()
    print(current_thread().name)
    sleep(2)
    num += 1
    lock.release()


# It's better to use lock with as context manager.


@process_timer
def main(number: int, func: Callable) -> None:
    list_of_threads = [create_thread(func) for _ in range(number)]
    for thread in list_of_threads:
        start_thread(thread)

    for thread in list_of_threads:
        join_thread(thread)


if __name__ == "__main__":
    main(12, add)
    print(" Done ".center(100, "*"))
