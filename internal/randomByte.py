import random

def randomByte():
    random.seed()
    number = random.random()

    if number >= 0.5:
        return "1"

    return "0"