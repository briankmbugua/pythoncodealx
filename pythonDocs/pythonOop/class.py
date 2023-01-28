#!/bin/python3.9

#A class named book for a book sales software


class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price

#instantiation
book1 = Book('Book 1',12, 'Author 1', 120)
book2 = Book('Book 2',18, 'Author 2', 220)
book3 = Book('Book 3',28, 'Author 3', 320)

print(repr(book1))


#encapsulation
"""process of preventing clients from accesing certain properties, which can only be accesed
through specific methods"""
#lets introduce a private attribute called __discount in the Book class

class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price
        self.__discount = 0.10

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"

book1 = Book('Book 1', 12, 'Author 1', 120)

print(book1.title)
print(book1.quantity)
print(book1.author)
print(book1.price)
print(book1.__discount)