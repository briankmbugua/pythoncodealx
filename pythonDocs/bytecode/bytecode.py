#!/bin/python3.9
#pythonbytecode
# """
# 1.Source code is not directly run by the target machine in interpreted languages, An interpreter program is used to execute the source code, it converts each statement of the source code into machine code, the interpreter is specific to the target machine, the interpreter reads and executes the source code directly

# 2.Python is a combination of compiled and interpreted language, the source code is compiled into bytecode, a low-level platform-indepedent representation of the source code.
# 3.The bytecode is not directly executable by the target machine, the bytecode is executed by the Python Virtual Machine, an interpreter specific to the target machine
# 4.The default implementation is CPyhton written in c, that compiles the code into bytecode and executes it with CPython virtual machine
# """

# #Generating bytecode files
# """
# in python the bytecode is stored in a .pyc file, in python3 the bytecode is stored in a folder name __pycache__.This folder is createda automatically when you try to import another file you created
# import file_name
# However it will not be created when if we don't import another file in the source code.
# It can be created manually from the command line

# python -m compileall file_1.py
# All .pyc files will be stored in the __pycache__ folder
# We  can also use the compile() function to compile a string that contains the python source code
# compile(source, filename, mode, flag, dont_inherit, optimize)
# source -- is the source code to compile which can be a string, bytes object, or an AST object
# filename -- is the name of the file that the source code comes from
# mode can be
# 'exec': accepts Python source code in any form, it compiles them into a bytecode that finally returns None
# 'eval': accepts a single expression and compiles it into bytecode that finally returns the value of that expression
# 'single': only accepts a single statement or multiple statements separated by ;
# """

c = compile("a=5 \na+=1 \nprint(a)", "", "exec")
print(type(c))
# """The compile function returns a python code object
# The code object can be executed or evaluated by passing it to the exec() or the eval() function
# """
d = compile("print(5)","","single")
eval(d)
exec(d)

# """When you define a function in python it creates the code object and you can access it using the __code__ attribute
# """

def f(n):
    return n

print(f.__code__)  

f(10)

c = compile("a=5 \na+=1 \nprint(a)", "", "exec")
print(type(c))

# """the type of c is code object, objects have many attributes, and to get the bytecode stored in a code object, you can use its co_code attribute"""
print(c.co_code) #b'd\x00Z\x00e\x00d\x017\x00Z\x00e\x01e\x00\x83\x01\x01\x00d\x02S\x00'
# """the result is byte literal which is prefixed with b', it is an immutable sequence of bytes and has a type of bytes
# Each byte can have a decimal value of 0 to 255, so a bytes literal is an immutable sequence of integers between 0 and 255
# Each interger can be represented as an ASCII character or in hexadecimal form with the escape sequence '\x'
# """


#Example
c = compile("print(10)","","single")
co_code = c.co_code
print("The compiled code as bytes literal:", co_code)
print("First byte: ", co_code[0])
print("The first byte in character format",chr(c.co_code[0]))
print("ASCII representation of the first byte", chr(co_code[0]))
print("Fourth byte ", co_code[4])
print("Hexadecimal representation of the fourth byte: ", hex(co_code[4]))

# """These sequence of bytes can be interpreted by CPython"""


#Bytecode details
#general opcode syntax which has an opcode and an oparg, each opcode has a human friendly name
#already have the opcodes in our bytecode, and we just need to map them to their corresponding opname
#we use the module dis to check
# """
# opcpde oparg
#     .
#     .
#     .
# """


bytecode = b'e\x00d\x00\x83\x01F\x00d\x01S\x00'
for byte in bytecode:
    print(byte, end=' ')
#output  101 0 100 0 131 1 70 0 100 1 83 0 
#first import dis
import dis
print(dis.opname[101])


