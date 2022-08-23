class Book:

    language = 'ENG'

    def show():
        print(Book.language)


book1 = Book()
book2 = Book()

print(book1.language)
print(book2.language)

Book.author = "Adam Mickiewicz"
print(Book.author)
print(book2.author)

book1.author = "Stanisław Len"

print(book2.author, book1.author)

print(book1.__dict__, book2.__dict__)
