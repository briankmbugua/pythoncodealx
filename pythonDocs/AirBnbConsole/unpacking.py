#!/usr/bin/python3
# record = ('dave', 'dev@example', '8994458484','3445677654')
# name, email, *phone_numbers = record

# print(name)
# print(email)
# print(phone_numbers)

# *trailling, current = [10, 8, 7, 1, 9, 5, 10, 3]
# print(trailling)
# print(current)


# records = [
#     ('foo', 1, 2),
#     ('bar', 'hello'),
#     ('foo', 3, 4)
# ]

# def do_foo(x, y):
#     print('foo', x, y)

# def do_bar(s):
#     print('bar', s)

# for tag, *args in records:
#     if tag == 'foo':
#         do_foo(*args)
#     elif tag == 'bar':
#         do_bar(*args)

# line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# uname, *fields, homedir, sh = line.split(':')

# print(uname)
# print(fields)
# print(homedir)
# print(sh)

items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(tail)


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))