#!/bin/python3.9

# positional arguments are a type of argument that are passed to a function or method by
# position, rather than by name
# When calling a function or method that accepts positional arguments, the values passed as arguments
# must be in the same order as the parameters defined in the function

def example_function(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

# example_function(1,2,3)

#FINAL FORMAL PARAMETERS

"""
A final formal parameter is a special syntax used in function or method definations to indicate
that any remaining positional arguments passed to the function should be collected into a tuple
A final formal parameter is defined by an asterisk (*) followed by the parameter name.
"""

#this function defination uses a final formal parameter to collect any additional positional
#arguments to a tuple called args

def final_formal_parameters(arg1,arg2,*args):
    print(arg1, arg2)
    print(args)

final_formal_parameters(1,2) # no additional arguments thus tuple will be empty
final_formal_parameters(1,2,3,4,5) # 1,2 (3,4,5) 3,4 and 5 are the additional arguments
                                   #and are collected in a tuple
"""
the fina formal parameter can also be used to collect any additonal keyword arguments to the
function into a dictionary called 'kwargs' to do this you use two asterisks(*)
"""
def keyword_args(arg1,arg2,*args,**kwargs):
    print('from keyword_args')
    print(arg1,arg2)
    print(args)
    print(kwargs)

keyword_args(1,2,3,4,5,keyword1=6,keyword2=7)
#from keyword_args
#1 2
#(3, 4, 5)
#{'keyword1': 6, 'keyword2': 7}
"""
when using final formal parameter, you can't use keyword arguments before it in a 
function call they should come after positional arguments
*param must occur before **param
"""
#function examples
"""consider the following function definations paying close attention to the markers / and *"""
def standard_arg(arg): 
    print(arg)
#no restriction on calling convention and args may be passed by position
#or keyword
standard_arg(2)
standard_arg(arg=2)

def pos_only_arg(arg, /):
    print(arg)
#can only use positional args as there is a / in the function    
pos_only_arg(1)
#pos_only_arg(arg=1)  TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'
def kwd_only_arg(*, arg):
    print(arg)
#kwd_only_args only allows keyword ar    
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only,standard,kwd_only)



