#!/bin/python3.9
"""the built-in variable '__name__' is used to determine if a python file is being
run as the main program or if it is being imported as a module into another program
When a python file is run directly, the special variable '__name__' is set to the string
"main" This allows you to include code in your script that should only be executed when the
script is run directly and not when it is imported as a module"""

#check if the script is the main program

if __name__ == "__main__":
    print('the script is being run directly')
