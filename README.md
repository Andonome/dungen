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
