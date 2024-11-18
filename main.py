#!/usr/bin/python

import phase1 as ph1
import phase2 as ph2
import phase3 as ph3
import graph as gph
import vars



def gogoDungeon(setting=vars.setting, dunSize=vars.dunSize, civilization=vars.civilization):
    dungeon = ph1.makeDungeon(setting, dunSize)
    ph2.civilize(dungeon)
    ph3.rampage(dungeon)
    gph.graph(dungeon, setting, civilization)
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
        testList = testDicPresence(i, vars.enemies, testList)
    return testList
