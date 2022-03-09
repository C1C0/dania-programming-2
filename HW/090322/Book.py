class Book:
    def __init__(self, isbn, title, author, publisher, pages, price, copies) -> None:
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__pages = pages
        self.__price = price
        self.__copies = copies
        
    def display(self) -> None:
        print(f"""---\nISBN: {self.__isbn}
TITLE: {self.__title}
AUTHOR: {self.__author}
PUBLISHER: {self.__publisher}
PAGES: {self.__pages}
PRICE: {self.__price}
COPIES: {self.__copies}\n---""")
    