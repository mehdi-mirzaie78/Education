# Thread Pool Executor
from concurrent.futures import ThreadPoolExecutor
from utils import process_timer
from time import sleep


def show(name):
    print(f'Starting {name} ...')
    sleep(3)
    print(f'Finishing {name} ...')


@process_timer
def main():
    # we can use max_workers for ThreadPoolExecutor to determine number of threads to be executed at the same time
    with ThreadPoolExecutor() as executor:
        names = ['One', 'Two', 'Three', 'Four', 'Five']
        executor.map(show, names)


if __name__ == "__main__":
    main()
