import utils
from threading import Thread
from time import sleep


def show(name, delay=3):
    print(f'Starting {name} ...')
    sleep(delay)
    print(f'Finishing {name}...')


class SubThread(Thread):
    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self) -> None:
        self.func(*self.args, **self.kwargs)


@utils.process_timer
def main():
    t1 = SubThread(show, 'markdown', 5)
    t2 = SubThread(show, 'mehdi', 7)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
