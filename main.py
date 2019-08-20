import sys

import yaml

from engine.cli import DjorkCli
from engine.text_engine import DjorkEngine

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Not enough arguments")
        sys.exit()
    world_file = sys.argv[1]

    with open(world_file) as world:
        world_desc = yaml.safe_load(world)

    eng = DjorkEngine()
    eng.fill_rooms(world_desc)
    eng.debug_info()
    eng.desc_current_room()
    cli = DjorkCli(engine=eng)
    cli.cmdloop()
