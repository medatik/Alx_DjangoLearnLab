# relationship_app/query_samples.py

import os
import django

# Setup Django environment manually
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")  # Replace with your project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "John Doe"
books_by_author = Book.objects.filter(author__name=author_name)
print(f"Books by {author_name}:")
for book in books_by_author:
    print(f"- {book.title}")

# List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
print(f"\nBooks in {library_name}:")
for book in library.books.all():
    print(f"- {book.title}")

# Retrieve the librarian for a library
librarian = library.librarian
print(f"\nLibrarian of {library_name}: {librarian.name}")
