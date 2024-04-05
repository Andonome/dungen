#!/usr/bin/python

# phase1 deals with stage 1: making the space
from phase1 import *
from phase2 import *
from phase3 import *
from graph import *
from vars import *

import random
import time


def gogoDungeon(setting=setting, dunSize=dunSize, civilization=civilization):
    dungeon = makeDungeon(setting, dunSize)
    civilize(dungeon)
    rampage(dungeon)
    graph(dungeon, setting, civilization)
    return dungeon


dungeon = gogoDungeon()

testList = {}


def testDicPresence(dungeon, dic, testList=testList):
    for f in dic:
        testList[f] = 0
        for x in dungeon:
            if f in x["features"]:
                testList[f] += 1
    return testList


def testD(noTests=10, testList=testList):
    for i in range(noTests):
        i = gogoDungeon()
        testList = testDicPresence(i, enemies, testList)
    return testList
