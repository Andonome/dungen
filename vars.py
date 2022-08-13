import random

# The TN function just rolls 2D6 to make choices.
def tn(tn):
    roll = random.randint(1,6) + random.randint(1,6)
    if roll >= tn:
        return True
    else:
        return False

# Just for debugging.
def show(x):
    pprint.pprint(x)

dunSize = random.randint(8,30)
print("Size: " + str(dunSize))
setting = random.choice(["mine", "caves"])

civilizations = [
    "elves",
    "dwarves",
    "gnomes",
]

civilization = random.choice(civilizations)

race = civilization

print("Race: " + civilization)

