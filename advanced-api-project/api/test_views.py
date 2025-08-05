from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Utilisateur authentifié
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()
        self.client.login(username="testuser", password="testpass")

        # Créer un auteur
        self.author = Author.objects.create(name="J.K. Rowling")

        # Créer un livre
        self.book = Book.objects.create(
            title="Harry Potter",
            publication_year=1997,
            author=self.author
        )

    def test_create_book(self):
        url = reverse("book-create")
        data = {
            "title": "Harry Potter 2",
            "publication_year": 1998,
            "author": self.author.id
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Harry Potter 2")

    def test_get_book_list(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_single_book(self):
        url = reverse("book-detail", kwargs={"pk": self.book.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Harry Potter")

    def test_update_book(self):
        url = reverse("book-update", kwargs={"pk": self.book.id})
        data = {"title": "Harry Potter Updated", "publication_year": 1997, "author": self.author.id}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Harry Potter Updated")

    def test_delete_book(self):
        url = reverse("book-delete", kwargs={"pk": self.book.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_filter_books_by_year(self):
        url = reverse("book-list") + "?publication_year=1997"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(book["title"] == "Harry Potter" for book in response.data))

    def test_search_books(self):
        url = reverse("book-list") + "?search=Harry"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Harry" in book["title"] for book in response.data))

    def test_order_books_by_title(self):
        Book.objects.create(title="A Book", publication_year=2000, author=self.author)
        url = reverse("book-list") + "?ordering=title"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book["title"] for book in response.data]
        self.assertEqual(titles, sorted(titles))


    def test_list_books_without_auth(self):
        self.client.logout()
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_without_auth(self):
        self.client.logout()
        url = reverse("book-create")
        data = {
            "title": "Not Allowed Book",
            "publication_year": 2020,
            "author": self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
