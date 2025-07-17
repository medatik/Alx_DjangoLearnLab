from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "John Doe"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
for book in books_by_author:
    print(book.title)

# List all books in a library
library = Library.objects.get(name="Central Library")
for book in library.books.all():
    print(book.title)

# Retrieve the librarian for a library
library = Library.objects.get(name="Central Library")
librarian = Librarian.objects.get(library=library)
print(librarian.name)
