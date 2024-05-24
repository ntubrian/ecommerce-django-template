
# E-commerce Project Setup

This project consists of a Django backend and a PostgreSQL database, all managed with Docker. Follow the steps below to set up and run the project.

## Prerequisites

- Docker and Docker Compose (Make sure Docker is installed)
- Python and Poetry

## Project Structure

```bash
ecommerce-backend/
├── business/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── ...
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── ...
├── docker-files/
│   ├── Dockerfile.backend
│   ├── docker-compose.yml
│   ├── nginx.conf
│   └── init.sql
├── manage.py
├── poetry.lock
├── pyproject.toml
└── README.md
```

## Setting Up the Environment

1. Create a new Django project using Poetry:

    ```bash
    mkdir backend
    cd backend
    
    poetry init --name ecommerce-backend --dependency django --dependency djangorestframework --dependency djangorestframework-simplejwt --dependency psycopg2 --dev-dependency black --dev-dependency isort --dev-dependency pylint --dev-dependency mypy

    poetry install
    poetry run django-admin startproject config .
    poetry run python manage.py startapp users
    poetry run python manage.py startapp business

    # Configure your python interpreter path in VS Code
    ```

2. Configure Django settings in `config/settings.py`:

    ```python
    # config/settings.py

    INSTALLED_APPS = [
        'rest_framework',
        'rest_framework_simplejwt',
        'users',
        'business',
        ...
    ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'ecommerce',
            'USER': 'postgres',
            'PASSWORD': 'password',
            'HOST': 'db',
            'PORT': '5432',
        }
    }

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
    }

    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
        'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    }
    ```

3. Create the `BusinessUser` model in `users/models.py`:

    ```python
    from django.db import models

    class BusinessUser(models.Model):
        ROLES = [
            ('admin', 'Admin'),
            ('store_manager', 'Store Manager'),
            ('product_manager', 'Product Manager'),
            ('order_manager', 'Order Manager'),
            ('customer_support', 'Customer Support'),
            ('finance_manager', 'Finance Manager'),
            ('marketing_specialist', 'Marketing Specialist'),
        ]
        username = models.CharField(max_length=255, unique=True)
        email = models.EmailField(unique=True)
        role = models.CharField(max_length=20, choices=ROLES)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        class Meta:
            db_table = 'business_users'
    ```

4. Create serializers, views, and URLs for `BusinessUser`:

    ```python
    # users/serializers.py
    from rest_framework import serializers
    from .models import BusinessUser

    class BusinessUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = BusinessUser
            fields = ['id', 'username', 'email', 'role']

    # users/views.py
    from rest_framework import viewsets
    from rest_framework.permissions import IsAuthenticated
    from .models import BusinessUser
    from .serializers import BusinessUserSerializer

    class BusinessUserViewSet(viewsets.ModelViewSet):
        queryset = BusinessUser.objects.all()
        serializer_class = BusinessUserSerializer
        permission_classes = [IsAuthenticated]

    # users/urls.py
    from django.urls import path, include
    from rest_framework.routers import DefaultRouter
    from .views import BusinessUserViewSet

    router = DefaultRouter()
    router.register(r'users', BusinessUserViewSet)

    urlpatterns = [
        path('api/', include(router.urls)),
    ]

    # config/urls.py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('users.urls')),
    ]
    ```

## Running the Project

1. Navigate to `docker-files` directory:

    ```bash
    cd docker-files
    ```

2. Start Docker Compose:

    ```bash
    docker-compose up --build
    ```

3. Open your browser and visit `http://localhost:8000/admin`. You should see the Django Admin interface.

4. Create a superuser:

    ```bash
    docker-compose exec backend poetry run python manage.py createsuperuser
    ```

## Setting Up the Environment for Development

1. Open a terminal and activate the Poetry shell:

    ```bash
    poetry shell
    ```

2. Check the path of the Python interpreter used by Poetry:

    ```bash
    which python
    ```

3. Copy the path displayed. In VS Code, press `Cmd + P` (or `Ctrl + P` on Windows/Linux) to open the command palette.

4. Type and select `Python: Select Interpreter`.

5. Choose `Enter interpreter path...`, then paste the path you copied from the `which python` command.

## Adding a New Entity or App via Django

1. Create a new app:

    ```bash
    poetry run python manage.py startapp new_app_name
    ```

2. Define models in the new app's `models.py`, create serializers, views, and URLs following the same pattern as the `users` app.

3. Add the new app to `INSTALLED_APPS` in `config/settings.py`.

4. Make and apply migrations:

    ```bash
    poetry run python manage.py makemigrations new_app_name
    poetry run python manage.py migrate
    ```

## Tech Stack

- **Django**: Web framework
- **Django REST Framework**: API framework
- **PostgreSQL**: Database
- **Docker**: Containerization
- **Poetry**: Dependency management
- **Pydantic**: Data validation and settings management
- **mypy**: Static type checker
- **black**: Code formatter
- **isort**: Import sorting tool
- **pylint**: Code linter

## Run Static type check

```bash
poetry run mypy .  
```

That's it! Your e-commerce project should now be up and running with Docker.
