#!/usr/bin/env python

# Default bot template

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
    output("Hello, friend")
    sleep(1)
    output('What can I do for you?')

def response(input):
    #print(input)
    if not respondToTrigger(input):
        output(randomResponse())
    # if respondToTrigger(input):
    #     pass
    # else:
    #     output(randomResponse())

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

def randomAssignment():
    answers = [
    "The assignment is to make a ChatBot, like me :)",
    "Code a working ChatBot",
    "Your ChatBot should talk to people",
    "You should code a Bot to chat with in Python"
    ]
    return random.choice(answers)

def respondToTrigger(input):
    global askedCounter
    trigger = [
    "assignment",
    "to do",
    "explain",
    "should i do"
    ]
    for t in trigger:
        if t in input:
            if askedCounter >1:
                output("You should understand by now...")
            output(randomAssignment())
            askedCounter += 1
            return True
    return False
