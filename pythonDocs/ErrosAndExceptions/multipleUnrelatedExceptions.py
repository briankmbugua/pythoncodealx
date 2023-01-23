#!/bin/python3.9
"""It is necessary to report several exceptions that have occured,this is often case
in concurrency frameworks, when several tasks may fail in parallel
Also there are cases where it is desirable to continue execution and collect multiple
errors rather than raise the first exception"""
"""
The built in ExceptionGroup wraps a list of exceptions instances so that they can be raised
togethor, it is an exception itself so it can be caught like any other exception
"""
class ExceptionGroup(Exception):
    def __init__(self, message, excs):
        super().__init__(message)
        self.excs = excs

def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)
f()

try:
    f()
except Exception as e:
    print(f'caught {type(e)}: e')
    