import random

dunSize = random.randint(8,30)
setting = random.choice(["mine", "caves"])

civilizations = [
    "elves",
    "dwarves",
    "gnomes",
]

civilization = random.choice(civilizations)

race = civilization

print("Race: " + civilization)

