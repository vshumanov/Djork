from typing import Optional

class Interactible():
    def __init__(self, *args, **kwargs):
        self.name: Optional[str] = kwargs.get("name", None)
        self.description: str = kwargs.get("description", None) 
        self.interact: Optional[str] = kwargs.get("interact", None)
        self.verb: Optional[str] = kwargs.get("verb", None)

    def __repr__(self):
        return f"<Interactible {self.name}, {self.description}>"
        