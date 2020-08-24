# from celery import shared_task
import random

# @shared_task
def get_number(): # noqa
    return random.random()
