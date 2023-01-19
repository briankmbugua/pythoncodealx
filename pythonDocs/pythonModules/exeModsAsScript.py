#!/bin/python3.9
"""the built-in variable '__name__' is used to determine if a python file is being
run as the main program or if it is being imported as a module into another program
When a python file is run directly, the special variable '__name__' is set to the string
"main" This allows you to include code in your script that should only be executed when the
script is run directly and not when it is imported as a module"""

#check if the script is the main program

if __name__ == "__main__":
    print('the script is being run directly')

"""When a python module is imported, '__name__' takes the name of the module"""

if __name__ == "module_name":
    print("this script is being imported as module")

#'__name__' is a built-in variable and it is always defined, so you can use it in any python
#script to help determine how the script is being run
#it's also worth noting that '__name__' can have a different value when the script is run from
#within an interactive python session, in that case it is set to '__main__'

import testModule

testModule.example() #output will this script is being imported as a module

