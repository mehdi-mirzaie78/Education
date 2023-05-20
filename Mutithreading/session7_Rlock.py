"""
    Rlock
"""

from threading import Thread, RLock, Lock

num = 0  # shared resource
# lock = Lock()
lock = RLock()
# We need to use Rlock because the lock acquired twice in the add function
# If we use Lock the program will be dead lock


def add():
    global num
    with lock:
        subtract()
        for _ in range(1000000):
            num += 1


def subtract():
    global num
    with lock:
        for _ in range(1000000):
            num -= 1


t = Thread(target=add)

t.start()

t.join()

print(num)

print("Done ...")
