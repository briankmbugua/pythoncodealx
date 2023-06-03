#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    file_storage = FileStorage()
    file_storage.reload()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF (Ctrl-D) is encountered"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            cls_id = args[1]
            obj = self.file_storage.find(cls_name, cls_id)
            if obj is None:
                print("** no instance found **")
                return
            print(obj)
        except IndexError:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            cls_id = args[1]
            obj = self.file_storage.find(cls_name, cls_id)
            if obj is None:
                print("** no instance found **")
                return
            self.file_storage.delete(obj)
            self.file_storage.save()
        except IndexError:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all instances or instances of a specific class"""
        args = arg.split()
        objs = []
        if not args:
            objs = self.file_storage.all().values()
        else:
            try:
                cls_name = args[0]
                objs = self.file_storage.get_objects_by_class(cls_name)
                if objs is None:
                    print("** class doesn't exist **")
                    return
            except NameError:
                print("** class doesn't exist **")
                return
        print("[{}]".format(", ".join(str(obj) for obj in objs)))

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            cls_id = args[1]
            obj = self.file_storage.find(cls_name, cls_id)
            if obj is None:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attribute = args[2]
            value = args[3]
            setattr(obj, attribute, value)
            self.file_storage.save()
            
        except IndexError:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

