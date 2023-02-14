#!/usr/bin/python3.9
import cmd

class HelloWorld(cmd.Cmd):
    def say_hi(self, args):
        name = args
        print(f'hi {name}')
    def exit(self):
        raise SystemExit

if __name__ == '__main__':
    HelloWorld = HelloWorld()
    HelloWorld.cmdloop("starting")