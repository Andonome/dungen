#!/usr/bin/python

import random

cause_list = [
    "depths",
    "mine"
]

location = random.choice(cause_list)

print("Location: " + location)

tunnel_area_list = []

if location == "depths":
    tunnel_area_list.append(["magma",1])
    tunnel_area_list.append(["tunnel",1])
    tunnel_area_list.append(["fungal garden",1])
    tunnel_area_list.append(["dome",1])
    tunnel_area_list.append(["small tunnel",1])
else:
    tunnel_area_list.append(["shallow river",1])
    tunnel_area_list.append(["deep river",1])
    tunnel_area_list.append(["supply room",1])
    tunnel_area_list.append(["deep shaft",1])
    tunnel_area_list.append(["mana lake",1])


map_locations = []

size = 6

while random.randint(0,len(map_locations)) < size:
    choice = random.choice(tunnel_area_list)
    if len(map_locations) == 0:
        map_locations.append(choice[0])
    else:
        if choice != map_locations[-1]:
            map_locations.append(choice[0])


print(map_locations)


print("\n")
