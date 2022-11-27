
<h1 align=center>Basic Celery</h1>

---

### Calling the function with celery

    add.delay(3, 4)
    add.apply_async(args=[3, 4], countdown=10)

apply_async provides more options for you. like countdown



### flower 


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




#### Some celery options 

For opening python shell:

    $ celery shell


For knowing the number of nodes(workers):

    $ celery status

#### Note: 
If we stop the celery and run this command we will get this response:
Error: No node replied within time constraint.


Erasing all the tasks:

    $ celery purge
    $ celery purge -f

#### WARNING: There's no undo for this operation, and messages will be permanently deleted!
##### -f is short for "force". you will no longer see the promt that pops up when you run "celery purge"

---

Seeing the list of active tasks(like flower you can see the details of the tasks):
    
    $ celery inspect active


List of scheduled ETA tasks: Shows the ones which were scheduled 
    
    $ celery inspect scheduled


List of reserved tasks:

    $ celery inspect reserved


Show worker statics:

    $ celery inspect stats


---

### Keeping Results

```python
app = Celery('tasks', backends='rpc://', broker='amqp://localhost')
```



### Config

for configuration we have 3 ways:
```
    1- Setting the options one by one which can be used for little configurations
        app.conf.option = option_value
        app.conf.task_serializer = 'json'
```

```
    2. Using update method of config which can be used for medium configurations

        app = Celery('one')
        app.conf.update(
            enable_utc = True,
            timezone = 'asia/tehran',
            task_serializer = 'json',   # yaml, pickle
            result_serializer = 'json',
            broker_url = 'amqp://localhost',
            result_backend = 'rpc://'
        )
```

```
    3. Using separate python config file which can be used for large configurations

        app.config_from_object('celeryconfig')
        # you should just write the name of the config file, no extension needed
```



#### Some options:

    broker_connection_retry
    broker_connection_max_retries
    import('name of the file') in config file
    worker_concurrency  ->  Default: Number of CPU cores
    worker_lost_wait    ->  Default: 10 seconds
    event_exchange
    control_exchange
    logging

