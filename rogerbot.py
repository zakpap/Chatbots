#!/usr/bin/env python

<<<<<<< HEAD
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
=======
# Roger bot

import chatServerModifyGlobals as c
import random


# Sleep and output functions
def sleep(n):
    c.sleep(n)


def output(s):
    c.output(s)


# Setup and Response function
def setup():
    global askedCounter, assignmentOrder
    global numCounter
    askedCounter = 0
    assignmentOrder = 0
    numCounter = 5
    output("Hello, my name is Roger.")
    sleep(1)
    output("What's up?")


def response(input):
    # print(input)
    if respondCounting(input):
        pass
    elif respondToTrigger(input):
        pass
    else:
        output(defaultRandomResponse())


def defaultRandomResponse():
    answers = [
        "Ok",
        "Roger",
        "Copy that",
        "Confirmative",
        "Affirmative",
        "Okay",
        "Okeydokey",
        "Yes",
        "Sure",
        "I agree",
        "Absolutely"
    ]
    response = random.choice(answers)
    return response


def orderedAssignmentDetails():
    global assignmentOrder
    scheme = "https://"
    githubRepo = "github.com/ArtezGDA/Course-Material"
    pageLink = "/blob/master/DesignAChatbot.md"
    answers = [
        "Design a chatbot!",
        "The assignment is to Design a Chatbot.",
        "A Chatbot. And you have to design its interactions.",
        """Read more about this Design a Chatbot Assignment
        at {}{}{}""".format(scheme, githubRepo, pageLink),
        "Make this chatbot more interesting.",
    ]
    if assignmentOrder < len(answers):
        response = answers[assignmentOrder]
        assignmentOrder += 1
    else:
        output("I don't know what else to say.")
        sleep(1.5)
        response = "Just go do it!"
    return response


def randomAgainRemarks():
    answers = [
        "Why do you ask me this again?",
        "What? Again?",
        "Do I have to repeat myself?",
        "Didn't you just hear me?",
        "Were you not listening?",
        "Ok. There we go. One more time",
        "For the last time,"
    ]
    return random.choice(answers)


def respondCounting(input):
    global numCounter
    if "count" == input:
        output("counting up to %d" % numCounter)
        numCounter += 1
        return True
    return False


def respondToTrigger(input):
    global askedCounter
    triggers = ["assignment", "what do I do", "chatbot"]
    for t in triggers:
        if t in input:
            if askedCounter > 1:
                output(randomAgainRemarks())
            output(orderedAssignmentDetails())
>>>>>>> ArtezGDA/master
            askedCounter += 1
            return True
    return False
