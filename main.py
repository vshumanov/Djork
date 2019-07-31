import json

from sys import argv, exit
from engine.text_engine import DjorkEngine

if __name__ == "__main__":
    if len(argv) < 2:
        print("Not enough arguments")
        exit()
    world_file = argv[1]

    with open(world_file) as world:
        world_desc = json.load(world)

    eng = DjorkEngine()
    eng.fill_rooms(world_desc)
    # eng.debug_info()
    eng.desc_current_room()
    eng.cmdloop()
    
    