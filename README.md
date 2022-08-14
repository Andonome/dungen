# Dun-Gen

This overly ambitious dungeon generator seeks to create a fantasy-style, tabletop RPG, dungeon.

## Plan

The script will attempt to create a dungeon, step by step, going through the dungeon's history.
It could start as the empty passages left by the flow of magma, or a tin-mine.

After that, a civilization establishes itself, traps can be made, and finally, a nasty bad-guy faction invades, populating the place with nasty things.

The script aims to make more plausible and engaging dungeons, by ensuring that every part has a reason to exist.

## Example

We start with randomly shifting rooms, then add features:

- a chasm
- river
- maybe a lake
- fungus growing around any water

Then some civilizing society (dwarves/ gnomes) comes in, digs out rooms and:

- makes the fungus into a proper fungal garden,
- creates living quarters,
- maybe a library,
- probably works of art.
- and traps the entrance.

Finally, tragedy arrives as a horde of monsters take over.
Suppose a necromancer comes along:

- dwarves become undead dwarves
- some traps no longer work
- the fungal garden becomes overrun by oozes

The computer then makes a description of each room, along with a very simple plot hook.

> You hear of an evil necromancer, inhabiting an old dwarven stronghold.

## Output

The result is an abstract map, made with `graphviz`.
I might make the map look good one day, but no time soon.

## Structure

The `dungeon` is a list, and each entry is a room.
`dungeon[0]` is the entrance.

Each entry in the list is a dictionary, detailing properties, features, et c.

Each entry has a list of places *below* that it joins to, forming the overall structure.

If room 8 has `connections = [-1, -4]`, then this means it connects to rooms 7 and 4.
All rooms only connect below them, to ensure that all rooms eventually lead to the exit.

## Position Types

The basic structure of everything is provided by the `types` entry in the dictionary.
Types include:

- tunnel (one connection in, one out)
- split (like above, but maybe multiple)
- dead ends (one join only)
- alternative paths (which you don't have to go down to reach the exit)

These types determine where rooms can go.
You don't want a kitchen in a tunnel, or everyone will wander through while you're trying to cook, and there's no use having a guard room in last area of the dungeon, after some marauder has travelled past the living area and treasure room.

```

                                                                                                                                                  ┌────────────────────────┐
                                                                                                                                                  │ 16: kitchen, foodStore │ <────────────────────────────────────────────────────────────────────────────────────────┐
                                                                                                                                                  └────────────────────────┘                                                                                          │
                                                                                                                                                                                                                                                                      │
                                                                                                                              ┌───────────────────────────────────────────────────────────────────────────┐                                                           │
                                                                                                                              ∨                                                                           ∨                                                           │
┌──────────────┐      ┌──────────────┐      ┌──────────────────┐      ┌──────────────┐      ┌────────────────────────┐      ┌──────────────┐      ┌⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯┐      ┌⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯┐      ┌⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯┐      ┌⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯┐  │
│      1:      │      │  2: bedroom  │      │ 3: river, bridge │      │      4:      │      │           5:           │      │  6: bedroom  │      ⋮                                              ⋮      ⋮      7:      ⋮      ⋮  8: bedroom  ⋮      ⋮  9: bedroom  ⋮  │
│ 5 hobgoblins │ <──> │ 4 hobgoblins │ <──> │                  │ <──> │ 5 hobgoblins │ <──> │      2 hobgoblins      │ <──> │ 3 hobgoblins │ <──> ⋮                                              ⋮ <──> ⋮ 5 hobgoblins ⋮ <──> ⋮ 1 hobgoblins ⋮ <──> ⋮ 1 hobgoblins ⋮  │
└──────────────┘      └──────────────┘      └──────────────────┘      └──────────────┘      └────────────────────────┘      └──────────────┘      ⋮                                              ⋮      └⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯┘      └⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯┘      └⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯┘  │
                                                                                                                              ∧                   ⋮                                              ⋮                                                    ∧               │
                                                                                                                              │                   ⋮                10: musicHall                 ⋮                                                    │               │
                                                                                                                              │                   ⋮                 4 hobgoblins                 ⋮ <──────────────────────────────────────────────────┘               │
                                                                                                                              ∨                   ⋮                                              ⋮                                                                    │
                                                                                            ┌────────────────────────┐      ┌──────────────┐      ⋮                                              ⋮                                                                    │
                                                                                            │ 15: kitchen, foodStore │      │     11:      │      ⋮                                              ⋮                                                                    │
                                                                                            │      1 hobgoblins      │      │ 3 hobgoblins │  ┌─> ⋮                                              ⋮ <──────────────────────────────────────────────────────────────────┘
                                                                                            └────────────────────────┘      └──────────────┘  │   └⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯┘
                                                                                              ∧                                               │     ∧                         ∧     ∧
                                                                                              │                                               │     │                         │     │
                                                                                              └───────────────────────────────────────────────┘     │                         │     │
                                                                                                                                                    ∨                         │     ∨
                                                                                                                                                  ┌────────────────────────┐  │   ┌──────────────┐
                                                                                                                                                  │       12: forge        │  │   │ 13: library  │
                                                                                                                                                  │      5 hobgoblins      │  │   │ 1 hobgoblins │
                                                                                                                                                  └────────────────────────┘  │   └──────────────┘
                                                                                                                                                  ┌────────────────────────┐  │
                                                                                                                                                  │      14: library       │  │
                                                                                                                                                  │      2 hobgoblins      │ <┘
                                                                                                                                                  └────────────────────────┘
```
