#!/usr/bin/python3
""" """


import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_quit(self, q):
        """Exits the program"""
        sys.exit()

    def do_EOF(self, eof):
        """Exits the program (usually due to end-of-file)"""
        sys.exit()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
