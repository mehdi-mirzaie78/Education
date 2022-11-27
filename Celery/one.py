from celery import Celery
from time import sleep

# app = Celery('one', backend='rpc://', broker='amqp://localhost')

# app.conf.timezone = 'asia/tehran'
# app.conf.enable_utc = True


# app.conf.update(
#     enable_utc = True,
#     timezone = 'asia/tehran',
#     task_serializer = 'json',   # yaml, pickle
#     result_serializer = 'json',
#     broker_url = 'amqp://localhost',
#     result_backend = 'rpc://'
# )


app = Celery('one')
app.config_from_object('conf')



@app.task
def add(x, y):
    sleep(5)
    return x + y
