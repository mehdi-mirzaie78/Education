# 2023-05-20 10:20:27
from threading import Thread, current_thread, enumerate
from time import sleep
from utils import process_timer


def show(name):
    # print(current_thread())
    print(enumerate())

    print(f'Starting {name} ...')
    sleep(3)
    print(f'Finishing {name} ...')


@process_timer
def main():
    t1 = Thread(target=show, args=('One',))
    t2 = Thread(target=show, args=('Two',))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(' Done '.center(100, '='))


if __name__ == "__main__":
    main()
