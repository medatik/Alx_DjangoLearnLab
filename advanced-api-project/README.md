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
