# cmd -- support for line-oriented command interpreters
The cmd module provides a simple framework for writting line-oriented command interpreters

## class cmd. Cmd(completekey='tab', stdin=None,stdout=None)
A Cmd instance or subclass instance is a line-oriented interpreter framework
There is no good reason to instantiate Cmd itself, rather it's useful as a superclass of an interpreter class you define yourself in order to inherit Cmd's methods and enscapulate action methods

### Arguments
- completekey(optional) defaults to tab, the key you will press to accept command completion
               if completekey is not None and readline is available, command completion is done automatically
- stdin and stdout(optional) specify the input and output of file objects that the Cmd instance or subclass instance will use for input and output.Default is sys.stdin and sys.stdout if not specified

# Cmd Objects
A Cmd instance has the following methods
- Cmd.cmdloop(intro=None) - Repeatedl issue a propmp, accept input, parse an initial prefix of the received input, and dispatch action methods, passing them the reminder of the line as argument
- Cmd.onecmd(str)
- Cmd.emptyline() - if an empty line is intered it repeats the last nonempty command entered
and several other methods reference python docs.