## API Endpoints for Book

| Method | Endpoint                | Description             | Auth |
|--------|-------------------------|-------------------------|------|
| GET    | /api/books/             | List all books          | No   |
| GET    | /api/books/<id>/        | Retrieve a book         | No   |
| POST   | /api/books/create/      | Create a new book       | Yes  |
| PUT    | /api/books/<id>/update/ | Update a book           | Yes  |
| DELETE | /api/books/<id>/delete/ | Delete a book           | Yes  |

### Notes:
- `publication_year` must not be in the future.
- Authenticated endpoints require session or token authentication.


## 📚 Book API — Filtering, Searching, and Ordering

### ✅ Filtering
- Filter by title: `/api/books/?title=Harry`
- Filter by author id: `/api/books/?author=3`
- Filter by year: `/api/books/?publication_year=1997`

### 🔍 Searching
- Search by title or author name: `/api/books/?search=Potter`

### 🔃 Ordering
- Order by title: `/api/books/?ordering=title`
- Descending order: `/api/books/?ordering=-publication_year`

# ✅ API Test Suite for Book Endpoints

### 🔬 What is tested?

- Book CRUD: create, read, update, delete
- Filtering by title, year, and author
- Searching by title or author
- Ordering results
- Permission controls: authenticated and anonymous access

### ▶️ How to run

```bash
python manage.py test api
