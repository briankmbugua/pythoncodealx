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
    
    def set_discount(self, discount):
        self.__discount = discount
    
    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
            return self.__price

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"

book1 = Book('Book 1', 12, 'Author 1', 120)

print(book1.title)
print(book1.quantity)
print(book1.author)
print(book1.price)
#print(book1.__discount)

single_book = Book('Two states', 1, 'chetan Bhagat', 200)
bulk_books = Book('Two states', 25, 'Chetan Bhagat', 200)
bulk_books.set_discount(0.20)

print(single_book.get_price())
print(bulk_books.get_price())
print(single_book)
print(bulk_books)