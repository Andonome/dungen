# Unsure how to do this part.  Some areas get built the
# same way - everyone needs a fungus garden and bridges
# over rivers.  But then some races will need different
# functions for where to build things.

import copy
import random
from features import *
from traps import *
from vars import *


def civilize(dungeon):
    placeContents(
    dungeon,
    civilFeatures,
    contentType = "civilized",
    race=civilization
    )
    placeContents(
    dungeon,
    traps,
    contentType = "traps",
    race = civilization
    )
