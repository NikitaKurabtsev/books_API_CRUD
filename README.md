CRUD operations with implementation of services and selectors layers.

## API CRUD operations with implementation of services and selectors layers.

### Collections/Resources

* Author

| Verb   | URL         | Descripton                                        | Scope              |
|--------|-------------|---------------------------------------------------|--------------------|
| GET    | /tshirt/    | Get the collection of T-shirts by ascending order | T-shirt Collection |
| GET    | /tshirt/id/ | Get a single T-shirt by id                        | T-shirt            |
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

* Category

| Verb   | URL         | Descripton                                        | Scope                  |
|--------|-------------|---------------------------------------------------|------------------------|
| GET    | /category/    | Get the collection of Categories by ascending order| Category Collection |
| GET    | /category/id/ | Get a single Category by id                        | Category            |
| PUT    | /category/id/ | Update a single Category by id                     | Category            |
| PATCH  | /category/id/ | Update one or more fields of an existing Category  | Category            |
| DELETE | /category/id/ | Delete a single Category by id                     | Category            |
| POST   | /category/id/ | Create a new Category in the collection            | Catgory Collection  |

* Color

| Verb   | URL         | Descripton                                        | Scope         |
|--------|-------------|---------------------------------------------------|---------------|
| GET    | /color/    | Get the collection of Colors by ascending order | Color Collection |
| GET    | /color/id/ | Get a single Color by id                        | Color            |
| PUT    | /color/id/ | Update a single Color by id                     | Color            |
| PATCH  | /color/id/ | Update one or more fields of an existing Color  | Color            |
| DELETE | /color/id/ | Delete a single Color by id                     | Color            |
| POST   | /color/id/ | Create a new Color in the collection            | Color Collection |

### Flow of data
**GET** -> Model -> Serializer -> JSONRenderer -> Response

**POST/PUT** -> JSONParser(request) -> Serializer -> Model -> JSONRenderer -> Response
