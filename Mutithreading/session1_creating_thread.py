from time import sleep
from threading import Thread
from utils import process_timer


def show(name):
    print(f'Starting {name} ...')
    sleep(3)
    print(f'Finishing {name}...')


# Running without multi thread takes twice of time
@process_timer
def main():
    print(" main is running ".center(50, '-'))
    show('One')
    show('Two')


@process_timer
def main2():
    print(" main2 is running ".center(50, '-'))
    t1 = Thread(target=show, args=('One',))
    t2 = Thread(target=show, args=('Two',))

    t1.start()
    t2.start()

    # This means that wait until it's fully finished
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()      # Took 6 seconds
    main2()     # Took 3 seconds
