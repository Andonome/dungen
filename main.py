#!/usr/bin/python

import phase1 as ph1
import phase2 as ph2
import phase3 as ph3
import graph as gph
import vars


TESTLIST = {}


def generate_dungeon(setting : str, dungeon_size : int, civilization : str, invaders : str):
    dungeon = ph1.generate_initial_layout(setting, dungeon_size)
    ph2.civilize(dungeon, civilization)
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
    dungeon_parameters = vars.generate_dungeon_parameters()
    dungeon = generate_dungeon(**dungeon_parameters)

if __name__ == "__main__":
    main()