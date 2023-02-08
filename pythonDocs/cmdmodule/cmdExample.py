#!/usr/bin/python3.9
from cmd import Cmd

class MyPrompt(Cmd):
    def do_hello(self, args):
         """Says hello if you provie a name it will greet you with"""
         if len(args) == 0:
            name = "stranger"
         else:
            name = args
         print("Hello", name)
    
    def do_quit(self, args):
        """Quits the programm."""

        print("Quitting")
        raise SystemExit

if __name__ == '__main__': #this means if the file is being executed directly and not as a module
    prompt = MyPrompt()
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt')