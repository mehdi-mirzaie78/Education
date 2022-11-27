# Working with signature

from time import sleep
from celery import Celery

app = Celery('two', backend='rpc://', broker_url='amqp://localhost')

@app.task
def add(x, y):
    sleep(5)
    return x + y

@app.task
def sub(x, y):
    return x - y

# result = add.signature( (3, 7) )
# result.delay()

# Partial
# partial = add.signature( (12, ) )
# partial.delay(23)


# Callbacks
# result = add.apply_async( (1, 9), link=sub.signature((3,)))
# 1 + 9 = 10    ->  10 - 3 = 7


# Immutablity: when the result of the first stage isn't important to the next stage 
# result = add.apply_async( (7, 2), link=sub.signature((10, 2), immutable=True) )
result = add.apply_async( (7, 2), link=sub.si(10,2))    # si = signature immutable
