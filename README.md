# DashPoints Backend

## Description
**DashPoints** is a purchase and points management system where users can accumulate points based on purchases made and exchange them for vouchers. The system features an administrative panel, REST APIs, and is prepared for integration with modern frontend systems.

## Technologies Used
- **Python 3.9**
- **Django 4.2**
- **Django REST Framework**
- **PostgreSQL** for the database.
- **Docker and Docker Compose** for managing the development and production environment.
- **Nginx** to serve the application in production.
- **GitHub Actions** for CI/CD, including automatic deployment on the VPS.
- **Swagger** for API documentation.
- **CORS Headers** for integration with frontend applications.
<!-- - **JWT** for secure authentication. -->
<!-- - **Phonenumbers** for phone number validation. -->

## Installation and Configuration

1. **Clone this repository:**

    ```bash
    git clone https://github.com/lucasfpac/dashpoints-backend.git
    cd dashpoints-backend
    ```

2. **Create and activate the virtual environment:**

    Using `pipenv`:

    ```bash
    pipenv install
    pipenv shell
    ```

    Or, if using `virtualenv`:

    ```bash
    virtualenv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Docker Configuration:**

    If you are using Docker, follow these steps:

    - **Create and start the containers:**

        ```bash
        sudo docker-compose up --build -d
        ```

    - **Run migrations and additional commands:**

        ```bash
        docker-compose exec web python manage.py makemigrations
        docker-compose exec web python manage.py migrate
        docker-compose exec web python manage.py createsuperuser  # Create optional superuser
        ```

5. **Database Migrations:**

    Apply migrations to create the tables:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Start the server:**

    Run the development server:

    ```bash
    python manage.py runserver
    ```

    Access the backend at `http://127.0.0.1:8000/`.

## Main Features

- **Purchase Management**: Register purchases associated with each user.
- **Points System**: Based on rules defined per event, accumulated points can be exchanged for vouchers.
- **Administrative Panel**: Interface to view and manage purchases, points, and users.
- **Report Generation**: Detailed reports of purchases and points.
- **API Documentation**: Access the API documentation via Swagger at `http://127.0.0.1:8000/dashpoints/swagger/`.
- **Frontend Integration**: Well-structured REST API for communication with frontend systems.
<!-- - **User Authentication System**: Login and registration of users using JWT. -->

## API Endpoints

### Customers
- **GET** `/customers/`  
  List all customers.
  
- **POST** `/customers/`  
  Create a new customer.

- **GET** `/customers/cpf_cnpj/{cpf_cnpj}/`  
  Retrieve a customer by CPF or CNPJ.

- **GET** `/customers/{id}/`  
  Customer details.

- **PUT** `/customers/{id}/`  
  Update customer information.

- **PATCH** `/customers/{id}/`  
  Partially update customer information.

- **DELETE** `/customers/{id}/`  
  Delete a customer.

### Events
- **GET** `/events/`  
  List all events.
  
- **POST** `/events/`  
  Create a new event.

- **GET** `/events/{id}/`  
  Event details.

- **PUT** `/events/{id}/`  
  Update event information.

- **PATCH** `/events/{id}/`  
  Partially update event information.

- **DELETE** `/events/{id}/`  
  Delete an event.

### Purchases
- **GET** `/purchases/`  
  List all purchases.
  
- **POST** `/purchases/`  
  Create a new purchase.

- **GET** `/purchases/{id}/`  
  Purchase details.

- **PUT** `/purchases/{id}/`  
  Update purchase information.

- **PATCH** `/purchases/{id}/`  
  Partially update purchase information.

- **DELETE** `/purchases/{id}/`  
  Delete a purchase.

### Stores
- **GET** `/stores/`  
  List all stores.
  
- **POST** `/stores/`  
  Create a new store.

- **GET** `/stores/{id}/`  
  Store details.

- **PUT** `/stores/{id}/`  
  Update store information.

- **PATCH** `/stores/{id}/`  
  Partially update store information.

- **DELETE** `/stores/{id}/`  
  Delete a store.

<!-- ## Directory Structure

- `core/`: Main application with general configurations.
- `purchases/`: Module responsible for registering and managing purchases and points.
- `api/`: Configuration and endpoints of the API.
- `dashboard/`: Panel for displaying aggregated data of purchases and users. -->

<!-- ## Tests

- **Automated Test Setup:**
  This project follows best practices with unit and integration tests, ensuring that new implementations do not break existing functionality.

- **Run Tests:**

    ```bash
    python manage.py test
    ``` -->

- **Integration with Git Hooks:**
  The project is set up to run automated tests before pushing to `main`, ensuring that only validated code is integrated.

## Best Practices and Deployment

The project follows best development practices:

- **CI/CD**: Pipeline configured with GitHub Actions for continuous deployment on the VPS, ensuring automatic integration of code from the `main` branch.
- **Branching Model**: Each new feature should be developed in its own branch and merged through Pull Requests, undergoing code review.
- **Automatic Deployment**: After merging into the `main` branch, automatic deployment on the VPS is done, with Docker commands to rebuild containers and migrate the database.

## Contribution

If you wish to contribute:

1. Fork this repository.
2. Create a branch with the new feature: `git checkout -b my-feature`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin my-feature`.
5. Open a Pull Request.

## License
This project is licensed under the MIT License.
