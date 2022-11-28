from bucket import bucket


# TODO: Can by async?
def all_objects_task():
    result = bucket.get_objects()
    return result
