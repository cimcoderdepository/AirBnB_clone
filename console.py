#!/usr/bin/python3
"""This module provides a console-like interpreter to handle input commands."""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Cmd console method."""

    prompt = "(hbnb) "
    __classes = ["BaseModel", "User"]

    def do_quit(self, arg):
        """Quit command to exit the program.
        """
        return True  # True for (1) means program run successful then quits.

    def do_EOF(self, arg):
        """Exit command to exit the program.
        """
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute anything."""
        return

    def do_create(self, arg):
        """Command interpreter: create command.

        Create new class instance, save it (to the JSON file),
        and print the id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_object = eval(f"{args[0]}")()
            print(new_object.id)

    def do_show(self, arg):
        """Command interpreter: show command.

        Print string representation of an instance based
        on the class name and id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        """Command interpreter: destroy command.

        Deletes an instance based on the class name and id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[f"{args[0]}.{args[1]}"]
        storage.save()

    def do_all(self, arg):
        """Command interpreter: all command.

        Prints all string representation of all instances based
        or not on the class name.
        """
        args = arg.split()
        if len(args) == 0:  # if args doesn't exist
            print([str(value) for value in storage.all().values()])
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            all_items = storage.all().items()
            print([str(v) for k, v in all_items if k.startswith(arg[0])])

    def do_update():
        """Command interpreter: update command.

        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
