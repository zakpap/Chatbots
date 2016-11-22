#!/usr/bin/env python

# Default bot template

import chatServer as c
import random

def setup():
    c.output("Hello, friend")
    c.sleep(1)
    c.output('What can I do for you?')

def response(input):
    #print(input)
    respondRandom()

def respondRandom():
    answers = [
    "Ok!",
    "You got it!",
    "Concider it done",
    "I'm already working on it!",
    "Yes, naturally.",
    "Ofcourse mate!"
    ]
    c.output(random.choice(answers))
