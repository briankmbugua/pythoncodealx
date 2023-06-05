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
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        try:
            value = obj_dict[key]
            print(value)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        class_id = args[1]
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        try:
            eval(class_name)
        except NameError:
            print("** class doesn't exist")
            return
        key = class_name + "." + class_id
        try:
            del obj_dict[key]
        except KeyError:
            print("** no instance found **")
        storage.save()

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
        storage = FileStorage()
        storage.reload()
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        key = args[0] + "." + args[1]
        obj_dict = storage.all()
        try:
            obj_value = obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        # try:
        #     attr_type = type(getattr(obj_value, args[2]))
        #     args[3] = attr_type(args[3])
        # except AttributeError:
        #     pass
        setattr(obj_value, args[2], args[3])
        obj_value.save()
    def emptyline(self):
        """Prevents printing anything when an empty line is passed"""
        pass
    def do_count(self, args):
        """Counts/retrieves the number of instances"""
        obj_list = []
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, val in objects.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    obj_list.append(val)
            else:
                obj_list.append(val)
        print(len(obj_list))
    def default(self, args):
        """Catches all the function names that are not explicitly defined"""
        functions = {"all": self.do_all, "update":self.do_update,"show": self.do_show, "count": self.do_count, "destroy": self.do_destroy, "update": self.do_update}
if __name__ == '__main__':
    HBNBCommand().cmdloop()

