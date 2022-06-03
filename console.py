#!/usr/bin/python3
"""The command interpreter for issue commands to our program."""


import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """The command interpreter"""
    prompt = "(hbnb) "
    def do_quit(self, q):
        """Exits the program"""
        sys.exit()

    def do_EOF(self, eof):
        """Exits the program (usually due to end-of-file)"""
        sys.exit()

    def create(self, obj):
        """Creates a new instance of BaseModel, saves it, & prints its ID"""
        newmodel = BaseModel()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
