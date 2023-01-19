# API CRUD operations with implementation of services and selectors layers.

## Test coverage 99%

## Django + DRF + Docker + Postgresql

### Collections/Resources

* Author

| Verb   | URL                 | Descripton                                       | Scope             |
|--------|---------------------|--------------------------------------------------|-------------------|
| GET    | /authors/           | Get the collection of authors                    | Authors Collection|
| POST   | /authors/create     | Create a new author in the collection            | Authors Collection|

* Books

| Verb   | URL                 | Descripton                                         | Scope             |
|--------|---------------------|----------------------------------------------------|-------------------|
| GET    | /books/             | Get the collection of bookss by ascending order    | Books Collection  |
| GET    | /books/id/          | Get a single book by id                            | Book              |
| PUT    | /books/update/id/   | Update a single book by id                         | Book              |
| DELETE | /books/delete/id/   | Delete a single book by id                         | Book              |
| POST   | /books/create/      | Create a new book in the collection                | books Collection  |