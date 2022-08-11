import random

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

