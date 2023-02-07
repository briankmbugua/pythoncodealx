# __init__.py
The package folder contains a special file called __init__.py, which stores the package's content it serves two purposes
- The python interpreter recognizes a folder as a package if it contains __init__.py file
- __init__.py file exposes specified resources from its module to be imported

An empty __init__.py file makes all functions from the above modules available when this package is imported

The __init__.py file is normally kept empty.However, it can also be used to choose specific functions from modules in the package folder and make them available for import