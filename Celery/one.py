from celery import Celery
from time import sleep

app = Celery('one', backend='rpc://', broker='amqp://localhost')

@app.task
def add(x, y):
    sleep(5)
    return x + y


# add.delay(3, 4)
# add.apply_async(args=[3, 4], countdown=10)
# apply_async provides more options for you. like countdown



############################# flower ##############################
"""

Open the cmd in the project directory and activate venv

    $ pip install flower

    $ celery flower -A one --broker=amqp://guest:guest@localhost:5672//

Open another cmd in the project directory and run:

    $ celery -A one worker -l info -P gevent

Open another cmd in the project directory and run:

    $ python

In python shell you can run these commands
and, will see how celery is making queues for the tasks:

    >>> from one import add
    >>> add.delay(8, 9)
    >>> add.apply_async(args=[5, 9])

Last but not least you can see the details in this page:

    localhost:5555

"""


############################# Some celery options ##############################
"""
For opening python shell:
    $ celery shell


For knowing the number of nodes(workers):
    $ celery status

# If we stop the celery and run this command we will get this response:
    Error: No node replied within time constraint.


Erasing all the tasks:
    $ celery purge
    $ celery purge -f

# WARNING: There's no undo for this operation, and messages will be permanently deleted!
# -f is short for "force". you will no longer see the promt that pops up when you run "celery purge"


Seeing the list of active tasks(like flower you can see the details of the tasks):
    $ celery inspect active


List of scheduled ETA tasks:
    $ celery inspect scheduled

# Shows the ones which were scheduled


List of reserved tasks:
    $ celery inspect reserved


Show worker statics:
    $ celery inspect stats




############################# Keeping Results ##############################

app = Celery('tasks', backends='rpc://', broker='amqp://localhost')


"""



