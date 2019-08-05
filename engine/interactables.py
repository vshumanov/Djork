from typing import Optional

class Interactable():
    def __init__(self, *args, **kwargs):
        self.name: Optional[str] = kwargs.get("name", None)
        self.description: str = kwargs.get("description", None) 
        self.interactions: dict = kwargs.get("interactions", None)

    def handle_result(self, action:str):
        act = self.interactions.get(action, None)
        if not act or not act['result']:
            return
        if act['result'] == "death":
            return "end"
        

    def __repr__(self):
        return f"<Interactible {self.name}, {self.description}> \n {self.interactions}"
        