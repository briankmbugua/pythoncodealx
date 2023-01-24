#!/bin/python3.9
#scopes and namespaces example before starting classes
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = 'global spam'

    spam = "test spam"
    do_local()
    print("After local assingment:", spam)
    do_nonlocal()
    print("After nonlocal assingment,", spam)
    do_global()
    print('After global assingment', spam)

scope_test()
print("In the global scope:", spam)


    