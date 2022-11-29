from bucket import bucket
from celery import shared_task


# TODO: Can by async?
def all_objects_task():
    result = bucket.get_objects()
    return result


@shared_task
def delete_object_task(key):
    bucket.delete_object(key)
