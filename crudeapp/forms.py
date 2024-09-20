from django import forms  # Import Django's forms module
from .models import Todo  # Import the Todo model from the current directory's models.py

class TodoForm(forms.ModelForm):  # Define TodoForm class, inheriting from Django's ModelForm
    class Meta:  # Inner Meta class to provide metadata to the form
        model = Todo  # Specify the model to base the form on
        fields = ['title', 'completed']  # List the fields to include in the form
        # or '__all__' # Alternative: include all fields from the model
        # Adjust fields as needed 