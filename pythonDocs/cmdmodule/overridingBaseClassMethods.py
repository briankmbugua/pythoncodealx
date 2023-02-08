#!/usr/bin/python3.9
#OVERRIDING BASE CLASS METHODS

import cmd

class Illustrate(cmd.Cmd):
    """Illustrate base class methods use"""
    def cmdloop(self, intro=None):
        print(f"cmdloop {intro}")
        return cmd.Cmd.cmdloop(self, intro)
    
    def preloop(self):
        print("preloop()")
    
    def postloop(self):
        print("postloop()")
    
    def parseline(self, line):
        print("parseline(%s) =>", line)
        ret = cmd.Cmd.parseline(self, line)
        print(ret)
        return ret
    def do_greet(self, line):
        print("hello",line)
    
    def do_EOF(self, line):
        "Exit"
        return True

if __name__ == "__main__":
    Illustrate().cmdloop("Illustrating the methods of cmd.Cmd")

    