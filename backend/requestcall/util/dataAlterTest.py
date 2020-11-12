import random
from .Convereter_trunc import truncater



def numberGen():
    number = truncater((random.random()*10)-5)
    return number
# print(number)

def listCreator(listLength):
    lst = []
    for i in range(listLength):
        lst.append(numberGen())
    return lst