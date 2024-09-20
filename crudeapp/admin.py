from django.contrib import admin  # Import the admin module from Django
from .models import Todo  # Import the Todo model from the current app's models.py

# Register your models here.

admin.site.register(Todo)  # Register the Todo model with the admin site - # Register the Todo model with the default AdminSite instance