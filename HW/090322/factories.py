from factory import fuzzy, Faker, Factory

from Book import Book
from random import randrange

class BookFactory(Factory):
    class Meta:
        model = Book

    isbn = Faker('isbn10')
    title = Faker('sentence')
    author = Faker('name')
    publisher = Faker('company')
    pages = fuzzy.FuzzyDecimal(10, 500)
    price = fuzzy.FuzzyDecimal(4, 99)
    copies = fuzzy.FuzzyDecimal(50, 100000)