#!/bin/python3.9
if __name__ == "testModule.py":
    print("This script is being imported as a module") #this will not be printed if we run this file directly as in ./testModule.py

if __name__ == 'main':
    print('this file is being run directly')
#call this function in the module where you will import this module
def example():
    print("This script is being imported as a module")



#if __name__ is the name of the module in this case testModule.py then the file is being imported as a module in another file else if the __name__ is 'main' then the file is being run directly and not imported as a module

