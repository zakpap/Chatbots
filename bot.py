#!/usr/bin/env python

# Default bot template

import chatServer as c
<<<<<<< HEAD

def setup():
    c.output("This is the bot template.")
    c.sleep(1)
    c.output('It does nothing more than just responding with "Ok".')

def response(input):
    print(input)
    c.output("Ok")

def respondRandom():
    answers = [
    "Ok!"
    "You got it!"
    "Concider it done"
    "Thanks, you too!"
    "Come on now!"
    "Hahaha!"
    ]
    c.output()
=======


# Sleep and output functions
def sleep(n):
    c.sleep(n)


def output(s):
    c.output(s)


def setup():
    output("This is the bot template.")
    sleep(1)
    output('It does nothing more than just responding with "Ok".')

    
def response(input):
    print(input)
    output("Ok")
>>>>>>> ArtezGDA/master
