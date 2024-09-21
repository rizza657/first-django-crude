from django.db import models
from django.utils import timezone

#parameters are variable that are defined in the fuction definition  

# Create your models here.

#models are schemas samples of the database structure 
#Migrations Implements the Behaviour of the models
#class Todo is a table name 
#CharField is a field type used in models to store short to medium-length strings.
class Todo(models.Model):  # Define Todo model, inheriting from Django's Model class
    title = models.CharField(max_length=100) # Create a character field for the title, max length 100
    completed = models.BooleanField(default=False)  # Create a boolean field for completion status, default is False
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):  # Define string representation of the Todo object
        return self.title  # Return the title when the object is printed


# The __str__ method defines how the object is represented as a string

#method is a function inside of a class


#This code  defines a data model in Django, which is often referred to as a "Model" or "Database Model".