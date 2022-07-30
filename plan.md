# Overview

The script will attempt to create a dungeon by making its own history.
It could start as the empty passages left by the flow of magma, or could begin as a gold-seem, and tunnelled out by greedy dwarves.

After that, a civilization establishes itself, traps can be made, and finally, a nasty bad-guy faction invades, populating the place with nasty things.

## Example

The program decides to make a mine, and draws some random elements:

`[ "chasm", "chasm", "alcove", "lake", "river", ]`

We replace the first element with an entrance, and we have a plausible mine layout.

`[ "entrance", "chasm", "alcove", "lake", "river", ]`

Now we decide which rooms connect to which (unsure how).

Next, a random civilization comes along, and make the place liveable, then adds rooms.


```
[
	"entrance (with trap)",
	"chasm (with bridge)",
	"alcove (now rooms)",
	"lake (with fishing boats)",
	"river (another bridge)",
	"living quarters",
	"chiseling hall",
	"runemaster library"
]
```

Finally, tragedy arrives as a horde of monsters take over.
Suppose a necromancer comes along:

```
[
	"entrance (with trap)",
	"chasm (with bridge)",
	"rooms (with undead dwarves)",
	"lake (full of undead dwarves)",
	"river (another bridge)",
	"living quarters (minor treasures and more undead)",
	"chiseling hall (where the treasure is, along with a weird undead creature)",
	"runemaster library (where the necromancer lives)"
]
```

The computer then makes a description of each room, along with a very simple plot hook.

> You hear of an evil necromancer, inhabiting an old dwarven stronghold.

# Timeline

## Location

- deep underground
- by the sea
- beneath a town
- middle of forest

## Tunnels

Tunnels are created.

- magma
- humans
- dwarves
- gnomes
- sewer system
- hidden castle
- giant prison

### Features

Possible features added here include:

- big chasm
- small alcove
- tiny tunnel
- long tunnel
- opening to underdark
- fungal garden
- river

## Civilization

Tunnels are expanded, and rooms carved out.

- dwarves
- goblins
- gnomes (lots of traps)
- humans (only available if lots of openness)
- wizard
- elves

At this point, the civilization converts things, and adds rooms, so a small alcove could become a room, or a long tunnel might become a hallway.

They add traps around entrances to safe-guard their stay, and block up tunnels to dangerous places with brick.

### Features

- entrance trap
- bedrooms
- tended garden
- illusion trap
- library
- underground garden
- banquet hall
- secret room
- prison

The civilizing race then updates old features, such as turning a chasm into a trap, or simply adds a bridge.
Rivers get used for food, fishing, et c.

## Invaders

The invaders come in through one entrance and destroy everyone they can.
An invading necromancer might turn the inhabitants to undead (producing undead gnomes, or dwarves, or whatever), and a dragon might burn all of them to death (leaving obvious corpses, and attracting oozes to eat the dead).

Any magical items will be taken by the invaders.

Secret rooms may not be discovered, so players might discover those rooms intact.

- goblins
- necromancer
- mad wizard
- dragon
- economic collapse

### Features

- side-tunnel (where the invaders broke in)
- barracks where the invaders set guards
- undead
- wandering monsters
- more traps

# Methods

- python
- ask Ross for ideas
- maybe use a bunch of classes?
- or maybe just start with lists of rooms, and attach descriptions later?
