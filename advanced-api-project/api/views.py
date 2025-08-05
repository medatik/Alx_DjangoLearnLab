from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# Accessible sans authentification
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Requiert l’authentification
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


"""
Views:
- BookListView: GET /books/ - Lists all books.
- BookDetailView: GET /books/<id>/ - Returns details of a single book.
- BookCreateView: POST /books/create/ - Creates a new book (auth required).
- BookUpdateView: PUT /books/<id>/update/ - Updates a book (auth required).
- BookDeleteView: DELETE /books/<id>/delete/ - Deletes a book (auth required).

Permissions:
- Read access is public.
- Write access is restricted to authenticated users.

Validation:
- BookSerializer prevents setting a publication_year in the future.
"""
