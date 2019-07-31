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
        
    def __repr__(self):
        """Used for printing the room on the screen."""
        return f"<Room : {self.name} {self.description} {self.options}>"

