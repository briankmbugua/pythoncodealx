#!/bin/python3.9
c = compile("print(10)","","single")
co_code = c.co_code
print("The compiled code as bytes literal:", co_code)
print("First byte: ", co_code[0])
print("ASCII representation of the first byte", chr(co_code[0]))
print("Fourth byte ", co_code[4])
print("Hexadecimal representation of the fourth byte: ", hex(co_code[4]))
