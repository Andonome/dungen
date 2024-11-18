#!/usr/bin/python

import phase1 as ph1
import phase2 as ph2
import phase3 as ph3
import graph as gph
import vars


TESTLIST = {}


def generate_dungeon(setting=vars.setting, dunSize=vars.dunSize, civilization=vars.civilization):
    dungeon = ph1.generate_dungeon_layout(setting, dunSize)
    ph2.civilize(dungeon)
    ph3.rampage(dungeon)
    gph.graph(dungeon, setting, civilization)
    return dungeon


def testDicPresence(dungeon, dic, testList=TESTLIST):
    for f in dic:
        testList[f] = 0
        for x in dungeon:
            if f in x["features"]:
                testList[f] += 1
    return testList


def testD(noTests=10, testList=TESTLIST):
    for i in range(noTests):
        i = generate_dungeon()
        testList = testDicPresence(i, vars.enemies, testList)
    return testList



def main():
    dungeon = generate_dungeon()

if __name__ == "__main__":
    main()