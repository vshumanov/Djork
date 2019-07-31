# Djork
Text adventure game engine

Currently there are no dependencies. Standard library only.

The engine works with a single world description file in json format.
All the rooms are described in the rooms object. 

Example.
  
``` json
"rooms": {
        "d_cave": {
            "name": "Dark Cave",
            "description": "A cave with little light in it. There is a sign on the wall",
            "options": {
                "north": "even_der_cave"
            },
            "interactibles": [
                "d_cave_sign"
            ]
        }
  }
```

Interactables can be defined in the world def file.


```json
"interactables": {
        "d_cave_sign": {
            "name": "Sign",
            "description": "A wooden sign",
            "interactions": {
                "read": "Go forth to eternal life. Go fifth and get a free toaster.",
                "touch": "It feels wooden and kind of damp."
            }
        }
    }
```

Should be added to each room they are supposed to be in the interactables object for the room.

```json
 "interactables": {
                "sign": "d_cave_sign"
            }
```

currently defined actions:

- read
- eat
- touch
- use
- punch


Running the game:

  Just instantiate the DjorkEngine class and use the fill_rooms method with the json object of the world description.
  Then start the cmdloop
  
``` python
with open("world_test.json") as world:
    world_desc = json.load(world)

eng = DjorkEngine()
eng.fill_rooms(world_desc)

if __name__ == "__main__":
    eng.debug_info()
    eng.desc_current_room()
    eng.cmdloop()
```

