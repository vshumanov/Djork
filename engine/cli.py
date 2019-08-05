"""Handle the DjorkEngine cli interface."""
import cmd
from .text_engine import DjorkEngine

class DjorkCli(cmd.Cmd):
    prompt = ">>>"

    def __init__(self, engine: DjorkEngine, *args, **kwargs):
        super().__init__()
        self.engine = engine

    def do_north(self, arg):
        """Move north."""
        self.engine.move_to("north")    
       
    def do_south(self, arg):
        """Move south."""
        self.engine.move_to("south")

    def do_west(self, arg):
        """Move to the west."""
        self.engine.move_to("west")

    def do_east(self, arg):
        """Move to the east."""
        self.engine.move_to("east")

    def do_look(self, arg):
        """Look around the current location."""
        self.engine.desc_current_room()

    def do_read(self, arg):
        """Read something."""
        self.engine.interact_with(action="read", target=arg)

    def do_eat(self, arg):
        """Eat something."""
        self.engine.interact_with(action="eat", target=arg)

    def do_touch(self, arg):
        """touch something."""
        self.engine.interact_with(action="touch", target=arg)

    def do_use(self, arg):
        """Use something."""
        self.engine.interact_with(action="use", target=arg)

    def do_punch(self, arg):
        """Punch something."""
        self.engine.interact_with(action="punch", target=arg)

    def do_inspect(self, arg):
        """Take a closer look at something."""
        self.engine.interact_with(action="inspect", target=arg)

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



    