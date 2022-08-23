from turtle import title


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

del book1.author

print(book1.__dict__, book2.__dict__)
print(book2.author, book1.author)

book1.title = 'Pan Tadeusz'
book2.year = 1995
print(book1.__dict__, book2.__dict__)
print("------------------------------------------------------Book 1--------------------------------")
class Book1:

    language = 'ENG'
    author = 'Mickiewicz'

print(Book1.__dict__)

books = [Book1(), Book1(), Book1()]
print(books)

for book in books:
    print(f"jezyk: {book.language}, author: {book.author}")

print("------------------------------------------------------Book titles--------------------------------")

titles = ["Sonety krumskie", 'Pan Tadeusz', 'Konrad Wallenrod']


for book, value in zip(books, titles):
    book.title = value

for book in books:
    print(f"jezyk: {book.language}, author: {book.author}, tytuł: {book.title}")

print("------------------------------------------------------Book titles 2--------------------------------")
titles = ["Sonety krumskie1", 'Pan Tadeusz2', 'Konrad Wallenrod3']


for book, value in zip(books, titles):
    setattr(book, 'title', value)

for book in books:
    print(book.__dict__)


