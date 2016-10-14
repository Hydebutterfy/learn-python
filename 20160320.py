__author__ = 'chenhaide'
import random


def generate():
    a = random.randrange(1, 10)
    b = random.randrange(1, 10)
    return "{} {}".format(a, b)

def generate1():
    return 42, "clue"

def generate2():
    return "question", "clue"

def generate3():
    return "question"

def generate4():
    return "question", 42


def solve(dataset):
    a, b = map(int, dataset.split())
    return str(a + b)


def check(reply, clue):
    return int(reply) == int(clue)

print(generate1(),generate2(),generate3(),generate4())