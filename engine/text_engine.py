import cmd
from .room import Room
from .interactibles import Interactible

class DjorkEngine(cmd.Cmd):
    prompt = ">>>"
    def __init__(self):
        super().__init__()
        self.rooms: dict = {}
        self.interactibles: dict = {}
        self.current_room: str = None

    def fill_rooms(self, world_desc: dict):
        for room_name, room_desc in world_desc["rooms"].items():
            n_room = Room(**room_desc)
            self.rooms[room_name] = n_room
            if self.current_room is None:
                self.current_room = room_name

        for int_name, int_desc in world_desc["interactibles"].items():
            n_int = Interactible(**int_desc)
            self.interactibles[int_name] = n_int

    def debug_info(self):
        print(f"Rooms :{self.rooms}")
        print(f"Interactibles: {self.interactibles}")
        print(f"Current : {self.current_room}")
        

    def desc_current_room(self):
        c_room = self.rooms[self.current_room]
        desc = f"{c_room.name}\n"
        desc += "-" * 60
        desc += "\n"
        desc += f"{c_room.description} \n"
        desc += "-" * 60
        
        print(desc)
        self.print_current_room_options()

    def print_current_room_options(self):
        c_room = self.rooms[self.current_room]
        for d, op in c_room.options.items():
            print(f"{d}: {self.rooms[op].name}")

    def move_to(self, direction:str):
        c_room = self.rooms[self.current_room]
        next_room = c_room.options.get(direction, None)
        if next_room:
            self.current_room = next_room
            c_room = self.rooms[self.current_room]
            print(f"You move to {c_room.name}")
            self.desc_current_room()
            # self.debug_info()
        else:
            print("Nothing in that direction")

    def do_north(self, arg):
        """Move north."""
        self.move_to("north")    
       
    def do_south(self, arg):
        """Move south."""
        self.move_to("south")

    def do_west(self, arg):
        """Move to the west."""
        self.move_to("west")

    def do_east(self, arg):
        """Move to the east."""
        self.move_to("east")

    def do_look(self, arg):
        """Look around the current location."""
        self.desc_current_room()

    def default(self, arg):
        print('I do not understand that command. Type "help" for a list of commands.')

    def do_quit(self, arg):
        """Quit the game."""
        return True # this exits the Cmd application loop.



    def __repr__(self):
        _repr = ""
        for room in self.rooms.values():
            _repr += f"{room.name} : {room.description} {room.options} \n"
        return _repr
