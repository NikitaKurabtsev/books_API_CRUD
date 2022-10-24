## API CRUD operations with implementation of services and selectors layers.

## DjangoDRF + Docker + Postgresql

### Collections/Resources

* Author

| Verb   | URL         | Descripton                                        | Scope              |
|--------|-------------|---------------------------------------------------|--------------------|
| GET    | /authors/    | Get the collection of T-shirts by ascending order | T-shirt Collection |
| GET    | /authors/id/ | Get a single T-shirt by id                        | T-shirt            |
| PUT    | /tshirt/id/ | Update a single T-shirt by id                     | T-shirt            |
| PATCH  | /tshirt/id/ | Update one or more fields of an existing T-shirt  | T-shirt            |
| DELETE | /tshirt/id/ | Delete a single T-shirt by id                     | T-shirt            |
| POST   | /tshirt/id/ | Create a new T-shirt in the collection            | T-shirt Collection |

* Books

| Verb   | URL         | Descripton                                        | Scope              |
|--------|-------------|---------------------------------------------------|--------------------|
| GET    | /brand/    | Get the collection of Brands by ascending order | Brand Collection      |
| GET    | /brand/id/ | Get a single Brand by id                        | Brand                 |
| PUT    | /brand/id/ | Update a single Brand by id                     | Brand                 |
| PATCH  | /brand/id/ | Update one or more fields of an existing Brand  | Brand                 |
| DELETE | /brand/id/ | Delete a single Brand by id                     | Brand                 |
| POST   | /brand/id/ | Create a new Brand in the collection            | Brand Collection      |

### Flow of data
**GET** -> Model -> Serializer -> JSONRenderer -> Response

**POST/PUT** -> JSONParser(request) -> Serializer -> Model -> JSONRenderer -> Response
