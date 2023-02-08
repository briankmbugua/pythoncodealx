#!/usr/bin/python3.9

# The help command is built into cmd
import cmd

class HelloWorld(cmd.Cmd):
    """simple command processer example"""#THIS IS A DOCSTRING
    def do_greet(self, person):#if a persons name is provided the greeting is personalized
        """greet [person]
        Greet the named person"""
        if person:
            print("Hi", person)
        else:
            print("hi")
    def do_EOF(self, line):
        """End the program"""
        return True
    def postloop(self):
        print()

if __name__ == '__main__':
    HelloWorld().cmdloop()