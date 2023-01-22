#!/bin/python3.9
"""The most common pattern for handling Exception is to print or log the exception and then
re-raise it(allowing a caller to handle the exception as well)"""
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print('Os error', err)
except ValueError:
    print("Could not convert data to an interger.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
