# get_object_or_404 ---- It retrieves an object from the database based on the given parameters.
#If the object is found, it returns it; if not, it raises a 404 Not Found error.


from django.shortcuts import render, redirect, get_object_or_404  # Import Django functions for rendering, redirecting, and 404 errors
from .models import Todo  # Import the Todo model from the current app
from .forms import TodoForm  # Import the TodoForm from the current app
#parameters are variable that are defined in the fuction definition  
# Function: index - Handles listing all todos and creating new ones
def index(request):
    todos = Todo.objects.all()  # Query function: Retrieve all Todo objects
    form = TodoForm()  # Form instantiation: Create a new TodoForm instance
    if request.method == 'POST':  # Conditional: Check if the request method is POST
        form = TodoForm(request.POST)  # Form instantiation: Create TodoForm with POST data
        if form.is_valid():  # Form validation: Check if the submitted data is valid
            form.save()  # Database operation: Save the new Todo object
            return redirect('index')  # Redirect function: Redirect to the index page
    return render(request, 'index.html', {'todos': todos, 'form': form})  # Render function: Display the index template
#RENDER: a user requests a web page, the server "renders" the content



# Function: update - Handles updating an existing todo
## Here, 'ck' is the parameter from the URL
#Todo.objects.get is a method
def update(request, ck):
    todo = Todo.objects.get(id=ck)  # Query function: Get a specific Todo object
    form = TodoForm(instance=todo)  # Form instantiation: Create TodoForm with existing Todo data
    if request.method == 'POST':  # Conditional: Check if the request method is POST
        form = TodoForm(request.POST, instance=todo)  # Form instantiation: Create TodoForm with POST data and existing Todo
        if form.is_valid():  # Form validation: Check if the submitted data is valid
            form.save()  # Database operation: Save the updated Todo object
            return redirect('index')  # Redirect function: Redirect to the index page
    return render(request, 'update.html', {'form': form, 'todo': todo})  # Render function: Display the update template

# Function: delete - Handles deleting an existing todo
def delete(request, ck):
    todo = get_object_or_404(Todo, id=ck)  # Query function - Get a Todo object or raise 404 if not found
    if request.method == 'POST':  # Conditional: Check if the request method is POST
        todo.delete()  # Database operation: Delete the Todo object
        return redirect('index')  # Redirect function: Redirect to the index page
    return render(request, 'delete.html', {'todo': todo})  # Render function: Display the delete template