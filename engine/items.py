class Item():
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get("name")
        self.description = kwargs.get("description")
        self.ground_description = kwargs.get("ground_description")
        self.states = kwargs.get("states")
        self.actions = kwargs.get("actions")

    def __repr__(self):
        return f'<Item {self.name} {self.description} '