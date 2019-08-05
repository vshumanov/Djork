"""Defining a 'room' or location."""


class Room():
    def __init__(self, *args, **kwargs):
        """Define a room with following parameters.
        
        name: str . unique name of the location
        description : str . short description of the location
        options: dict. the name of the location in that direction.
        interactions: dict.  interactables in the room
        """

        self.name:str = kwargs.get("name")
        self.description:str = kwargs.get("description")
        self.options:dict = kwargs.get("options")
        self.interactables: list = kwargs.get("interactables")
        
    def describe(self):
        desc = f"{self.name}\n"
        desc += "-" * 60
        desc += "\n"
        desc += f"{self.description} \n"
        desc += "-" * 60
        print(desc)

    def show_options(self):
        for d, op in self.options.items():
            print(f"{d}: {op}")

    def __repr__(self):
        """Used for printing the room on the screen."""
        return f"<Room : {self.name} \n {self.description} \n {self.options}>"

