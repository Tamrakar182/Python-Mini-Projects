import random

def cointoss():
    number = random.randint(0, 1)
    if number == 0:
        print("tails")
    if number == 1:
        print("heads")

cointoss()