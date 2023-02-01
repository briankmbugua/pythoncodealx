#!/usr/bin/python3.9
c = compile("a=5 \na+=1 \nprint(a)", "", "exec")
print(type(c))
