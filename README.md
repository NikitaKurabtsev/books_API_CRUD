## API CRUD operations with implementation of services and selectors layers.

## DjangoDRF + Docker + Postgresql

### Collections/Resources

* Author

| Verb   | URL          | Descripton                                       | Scope             |
|--------|------------- |--------------------------------------------------|-------------------|
| GET    | /authors/    | Get the collection of authors                    | Author Collection |
| GET    | /authors/id/ | Get a single author by id                        | Author            |
| PUT    | /authors/id/ | Update a single author by id                     | Author            |
| PATCH  | /authors/id/ | Update one or more fields of an existing author  | Author            |
| DELETE | /authors/id/ | Delete a single author by id                     | Author            |
| POST   | /authors/id/ | Create a new author in the collection            | Author Collection |

* Books

| Verb   | URL          | Descripton                                         | Scope             |
|--------|--------------|----------------------------------------------------|-------------------|
| GET    | /books/      | Get the collection of bookss by ascending order    | books Collection  |
| GET    | /books/id/   | Get a single book by id                            | books             |
| PUT    | /books/id/   | Update a single book by id                         | books             |
| PATCH  | /books/id/   | Update one or more fields of an existing book      | books             |
| DELETE | /books/id/   | Delete a single book by id                         | books             |
| POST   | /books/id/   | Create a new book in the collection                | books Collection  |

### Flow of data
**GET** -> Model -> Serializer -> JSONRenderer -> Response

**POST/PUT** -> JSONParser(request) -> Serializer -> Model -> JSONRenderer -> Response
