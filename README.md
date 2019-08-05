# Djork
Text adventure game engine

Currently there are no dependencies. Standard library only.

The engine works with a single world description file in yaml format.
All the rooms are described in the rooms object. 

Example.
  
``` yaml

rooms:
  d_cave:
    name: Dark Cave
    description: A cave with little light in it. There is a sign on the wall
    options:
      north: even_der_cave
  even_der_cave:
    name: Even darker cave
    description: A cave with even less light in it
    options:
      south: d_cave

```

Interactables can be defined in the world def file.


```yaml
interactables:
  d_cave_sign:
    name: Sign
    description: A wooden sign
    interactions:
      read: Go forth to eternal life. Go fifth and get a free toaster.
      touch: It feels wooden and kind of damp.

```

Should be added to each room they are supposed to be in the interactables object for the room.

```yaml
 d_cave:
    name: Dark Cave
    description: A cave with little light in it. There is a sign on the wall
    options:
      north: even_der_cave
    interactables:
      sign: d_cave_sign
```

currently defined actions:

- read
- eat
- touch
- use
- punch


Running the game:

  Run the main script with the world file as argument
  
``` 
python main.py world_def.yaml
```

