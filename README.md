## API CRUD operations with implementation of services and selectors layers.

## DjangoDRF + Docker + Postgresql

### Collections/Resources

* Author

| Verb   | URL          | Descripton                                       | Scope             |
|--------|------------- |--------------------------------------------------|-------------------|
| GET    | /authors/    | Get the collection of authors                    | Authors Collection|
| GET    | /authors/id/ | Get a single author by id                        | Author            |
| PUT    | /authors/id/ | Update a single author by id                     | Author            |
| PATCH  | /authors/id/ | Update one or more fields of an existing author  | Author            |
| DELETE | /authors/id/ | Delete a single author by id                     | Author            |
| POST   | /authors/    | Create a new author in the collection            | Authors Collection|

* Books

| Verb   | URL          | Descripton                                         | Scope             |
|--------|--------------|----------------------------------------------------|-------------------|
| GET    | /books/      | Get the collection of bookss by ascending order    | Books Collection  |
| GET    | /books/id/   | Get a single book by id                            | Book              |
| PUT    | /books/id/   | Update a single book by id                         | Book              |
| PATCH  | /books/id/   | Update one or more fields of an existing book      | Book              |
| DELETE | /books/id/   | Delete a single book by id                         | Book              |
| POST   | /books/      | Create a new book in the collection                | books Collection  |