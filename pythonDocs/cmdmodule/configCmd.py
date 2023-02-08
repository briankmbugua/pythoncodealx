#!/usr/bin/python3.9

#prompt can be used to set a string to be printed each time the user is asked for a new command
#intro is the 'welcome' message printed at the start of the program
#cmdloop() takes an argument for this value or you can set it on the class directly
#When printing help the doc_header, misc_header, undoc_header and ruler attributes are used to format the output

#example class shows a command processor to let the user control the prompt for interactive session

import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example"""
    prompt = "prompt "
    intro = "Simple command processor example"

    doc_header = "doc_header"
    misc_header = "misc_header"
    undoc_header = "undoc_header"

    ruler = "_"