#!/usr/bin/python3.9
# the uuid module provides immutable UUID objects(the UUID class) and the functions uuid1(),uuid3(), uuid4(), uuid5()
#if all you want is a unique ID, you should probably call uuid1() or uuid4(), Note that uuid1() may compromise security since it creates a UUID containing the computer's network address
#uuid1() may or may not return a "safe" UUID.All instances of UUID have an is_safe attribute which relays any information about the UUID'S safety


#EXAMPLE

import uuid

#make a UUID based on the host ID and current time
id1 = uuid.uuid1()
id2 = uuid.uuid1()

# print(id1)
# print(id2)

#make a random UUID
id3 = uuid.uuid4()
id4 = uuid.uuid4()

# print(id3)
# print(id4)

stringId = str(id4)
print(stringId)