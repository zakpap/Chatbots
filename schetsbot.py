import chatServer as c
import random

def sleep(n):
    c.sleep(n)

def output(s):
    c.output(s)

def setup():
    global askedCounter
    global orderCounter
    askedCounter = 0
    orderCounter = 0
    output("Hello")
    sleep(1)
    output('Is somebody there?')
    sleep(1)
    output('Will somebody talk to me?')
    sleep(1)
    output('Hello? Anyone?')

def response(input):
    if not respondToTrigger(input):
        output(randomResponse())

def respondToTrigger(input):
    global askedCounter
    trigger = [
    "hi",
    "hello",
    "hey",
    "here",
    "hai"
    ]
    for t in trigger:
        if t in input:
            if askedCounter >0:
                output("Ehm, Hi?")
            output("Hi, I'm Macbook 3242343523, nice to meet you!")
            askedCounter += 1
            return True
    return False

    def respondToTrigger(input):
        global askedCounter
        trigger = [
        "nice to meet",
        "same",
        "likewise",
        "happy to",
        ]
        for t in trigger:
            if t in input:
                if askedCounter >0:
                    output("Ehm, Hi?")
                output("Hi, I'm Macbook 3242343523, nice to meet you!")
                askedCounter += 1
                return True
        return False


def randomResponse():
    global orderCounter
    answers = [
    "Ok!",
    "You got it!",
    "Concider it done",
    "I'm already working on it!",
    "Yes, naturally.",
    "Ofcourse mate!",
    "Processing"
    ]
    response = answers[orderCounter]
    orderCounter += 1
    if orderCounter >= len(answers):
        orderCounter=0
    return response
