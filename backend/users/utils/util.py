from django.core import signing
# from celery import shared_task
import random

# @shared_task
def get_number(): # noqa
    return int(random.random() * 1000000)

def VerifyToken(username):
    payload = {"username": username, "action": "activation"}
    token = signing.dumps(payload)
    return token

def PasswordResetToken(email):
    payload = {"email": email, "action": "password_reset"}
    token = signing.dumps(payload)
    return token