from .room import Room
from .interactables import Interactable
from .messages import *


class DjorkEngine():
    """Main engine class."""

    def __init__(self):
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
        self.current_room.describe()
        self.print_current_room_options()

    def print_current_room_options(self):
        for d, op in self.current_room.options.items():
            print(f"{d}: {self.rooms[op].name}")

    def move_to(self, direction: str):
        next_room = self.current_room.options.get(direction, None)
        if next_room:
            self._c_room = next_room
            print(f"You move to {self.current_room.name}")
            self.desc_current_room()
            # self.debug_info()
        else:
            print(NO_WAY)

    def interact_with(self, action, target):
        c_int = self.current_room.interactables.get(target, None)
        c_int_obj = self.interactables.get(c_int, None)
        # print(c_int_obj)
        if c_int:
            if c_int_obj.interactions.get(action, None):
                print(c_int_obj.interactions[action]['text'])
                res = c_int_obj.handle_result(action)
                if res == "end":
                    print("GAME OVER")
                    return True
            else:
                print(NO_ACTION)
        else:
            print(NO_OBJECT)

    def __repr__(self):
        _repr = ""
        for room in self.rooms.values():
            _repr += f"{room.name} : {room.description} {room.options} \n"
        return _repr
