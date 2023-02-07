#!/usr/bin/python3.9

# Install a Package Globally

# Once a package is created, it can be installed for system wide use by running the setup script, The script calls the setup() function from the setuptools module

# The script calls the setup() funtion which takes various arguments such as name, version, author, list of depedencies, etc. The zip_safe argument defines whether the package is installed in compressed mode or regular mode


from setuptools import setup

setup(name='mypackage',
version='0.1',
description='Testing installation of Package',
url='#',
author='brian',
author_email='briankmbugua@email.com',
license='MIT',
packages=['mypackage'],
zip_safe=False)