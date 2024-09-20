from django.db import models




# Create your models here.

#models are schemas samples of the database structure 
#Migrations Implements the Behaviour of the models
#class Todo is a table name 
class Todo(models.Model):  # Define Todo model, inheriting from Django's Model class
    title = models.CharField(max_length=100)  # Create a character field for the title, max length 100
    completed = models.BooleanField(default=False)  # Create a boolean field for completion status, default is False

    def __str__(self):  # Define string representation of the Todo object
        return self.title  # Return the title when the object is printed


# The __str__ method defines how the object is represented as a string

#method is a function inside of a class