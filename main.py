import json
from engine.text_engine import DjorkEngine

with open("world_test.json") as world:
    world_desc = json.load(world)

eng = DjorkEngine()
eng.fill_rooms(world_desc)

if __name__ == "__main__":
    eng.debug_info()
    eng.desc_current_room()
    eng.cmdloop()
    
    