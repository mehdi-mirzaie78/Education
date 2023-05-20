from time import sleep
from threading import Thread
from utils import process_timer
import sys


def show(name):
    print(f'Starting {name} ...')
    sleep(5)
    print(f'Finishing {name}...')


@process_timer
def main():
    print(" main is running ".center(50, '-'))
    # Daemon is False by default which means that the program can't ignore threads
    # t1 = Thread(target=show, args=('One',))
    # t2 = Thread(target=show, args=('Two',))

    # Daemon is True
    t1 = Thread(target=show, args=('One',), daemon=True)
    t2 = Thread(target=show, args=('Two',), daemon=True)

    t1.start()
    t2.start()


main()  # Took 6 seconds
sys.exit()
