import cmd
from .room import Room
from .interactables import Interactable

class DjorkEngine(cmd.Cmd):
    prompt = ">>>"
    def __init__(self):
        super().__init__()
        self.rooms: dict = {}
        self.interactables: dict = {}
        self._c_room: str = None

    @property
    def current_room(self):
        return self.rooms[self._c_room]

    def fill_rooms(self, world_desc: dict):
        for room_name, room_desc in world_desc["rooms"].items():
            n_room = Room(**room_desc)
            self.rooms[room_name] = n_room
            if self._c_room is None:
                self._c_room = room_name

        for int_name, int_desc in world_desc["interactables"].items():
            n_int = Interactable(**int_desc)
            self.interactables[int_name] = n_int

    def debug_info(self):
        print(f"Rooms :{self.rooms}")
        print(f"Interactables: {self.interactables}")
        print(f"Current : {self.current_room}")
        

    def desc_current_room(self):
        desc = f"{self.current_room.name}\n"
        desc += "-" * 60
        desc += "\n"
        desc += f"{self.current_room.description} \n"
        desc += "-" * 60
        
        print(desc)
        self.print_current_room_options()

    def print_current_room_options(self):
        for d, op in self.current_room.options.items():
            print(f"{d}: {self.rooms[op].name}")

    def move_to(self, direction:str):
        next_room = self.current_room.options.get(direction, None)
        if next_room:
            self._c_room = next_room
            print(f"You move to {self.current_room.name}")
            self.desc_current_room()
            # self.debug_info()
        else:
            print("Nothing in that direction")

    def interact_with(self, action, target):
        c_int = self.current_room.interactables.get(target, None)
        c_int_obj = self.interactables.get(c_int, None)
        # print(c_int_obj)
        if c_int:
            if c_int_obj.interactions.get(action, None):
                print(c_int_obj.interactions[action])
            else:
                print("That's a silly thing to do")
        else:
            print("No such object around you")

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

    def do_read(self, arg):
        """Read something."""
        self.interact_with(action="read", target=arg)

    def do_eat(self, arg):
        """Eat something."""
        self.interact_with(action="eat", target=arg)

    def do_touch(self, arg):
        """touch something."""
        self.interact_with(action="touch", target=arg)

    def do_use(self, arg):
        """Use something."""
        self.interact_with(action="use", target=arg)

    def do_punch(self, arg):
        """Punch something."""
        self.interact_with(action="punch", target=arg)

    def do_inspect(self, arg):
        """Take a closer look at something."""
        self.interact_with(action="inspect", target=arg)

    def do_give(self, arg):
        """Give something to someone.
        
        FIXME Pass 2 parameters.
        """
        raise NotImplementedError

    def do_take(self, arg):
        """Take something and put it in your bag.
        
        TODO implement inventory.
        """
        raise NotImplementedError

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
    