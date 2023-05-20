from threading import Event, Thread
from time import sleep

"""
Event is used for two threads executes exactly at the same time
The threads wait to be executed together
"""


# When we use event we don't have to use join remember that


def first(f: Event, s: Event) -> None:
    print('First is ready...')
    f.set()
    s.wait()
    print('First is working...')
    f.clear()


def second(f: Event, s: Event) -> None:
    print('Second is ready...')
    s.set()
    f.wait()
    print('Second is working...')
    s.clear()


f = Event()
s = Event()

t1 = Thread(target=first, args=(f, s))
t2 = Thread(target=second, args=(f, s))

t1.start()
t2.start()
