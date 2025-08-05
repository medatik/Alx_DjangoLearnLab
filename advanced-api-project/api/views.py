from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Accessible sans authentification
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # 👇 Activation du filtrage, de la recherche, et de l'ordonnancement
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # 👇 Champs filtrables : par titre, année et id d'auteur
    filterset_fields = ['title', 'publication_year', 'author']

    # 👇 Recherche texte dans ces champs (en LIKE)
    search_fields = ['title', 'author__name']

    # 👇 Champs autorisés pour l'ordonnancement
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # ordre par défaut

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
"""
BookListView:
- Supports filtering on 'title', 'publication_year', and 'author'.
- Supports full-text search on 'title' and 'author name'.
- Supports ordering on 'title' and 'publication_year'.

Example queries:
- /api/books/?title=Harry
- /api/books/?search=Rowling
- /api/books/?ordering=publication_year
- /api/books/?search=Potter&ordering=-title
"""
