# Domino Disruption Predictor (DDP)

This project aims to build a complete web application that tracks micro-disruptions, detects root causes, identifies recurring patterns, calculates total impact, and predicts next probable disruptions using sequence statistics.

## Project Structure

- `ddp_project/`: The main Django project.
- `core/`: The Django application containing models, serializers, views, and URLs for the DDP functionalities.
- `frontend/`: (To be created) Contains the HTML, CSS, and JavaScript for the user interface.

## Setup and Installation

Follow these steps to set up and run the project locally:

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository_url>
    cd DDP
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install Django djangorestframework djangorestframework-simplejwt
    ```

5.  **Apply database migrations:**
    ```bash
    python manage.py makemigrations core
    python manage.py migrate
    ```

6.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create an admin user.

7.  **Run the Django development server:**
    ```bash
    python manage.py runserver
    ```
    The backend API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

The following API endpoints are available:

-   `/api/auth/register/` (POST): User registration.
-   `/api/auth/login/` (POST): User login, returns JWT tokens.
-   `/api/auth/token/` (POST): Obtain new access token using refresh token.
-   `/api/auth/token/refresh/` (POST): Refresh access token.
-   `/api/tags/` (GET, POST): List and create tags.
-   `/api/tags/<int:pk>/` (GET, PUT, DELETE): Retrieve, update, and delete a specific tag.
-   `/api/disruption/` (GET, POST): List and create disruption entries for the authenticated user.
-   `/api/disruption/<int:pk>/` (GET, PUT, DELETE): Retrieve, update, and delete a specific disruption entry.
-   `/api/disruption/user/` (GET): List disruption entries for the authenticated user.
-   `/api/root-cause-rules/` (GET, POST): List and create root cause rules (Admin only).
-   `/api/root-cause-rules/<int:pk>/` (GET, PUT, DELETE): Retrieve, update, and delete a specific root cause rule (Admin only).
-   `/api/suggestion-templates/` (GET, POST): List and create suggestion templates (Admin only).
-   `/api/suggestion-templates/<int:pk>/` (GET, PUT, DELETE): Retrieve, update, and delete a specific suggestion template (Admin only).

## Frontend

The frontend will be developed using HTML5, CSS3, and JavaScript, communicating with the backend via `fetch()` requests. Details will be added here once the frontend is implemented.

## Next Steps

-   Implement prediction logic and dashboard APIs.
-   Develop the frontend UI.
-   Add sample data seeds.
-   Provide Postman/cURL examples.
-   Add deployment instructions.