# get_object_or_404 ---- It retrieves an object from the database based on the given parameters.
# If the object is found, it returns it; if not, it raises a 404 Not Found error.
# redirect ---- It can be used in views to navigate users away from the current page, 
# typically after performing an action like submitting a form.
# render ---- Combines a given template with a context dictionary and returns an HttpResponse object.
from django.shortcuts import render, redirect, get_object_or_404  # The django.shortcuts -- module provides essential functions that streamline common tasks in Django views, making it easier to handle rendering, redirects, and error handling efficiently.
from .models import Todo  # Import the Todo model from the current app
from .forms import TodoForm  # Import the TodoForm from the current app
# parameters are variable that are defined in the fuction definition  
# Function: Functions are reusable blocks of code designed to perform a specific task. 
# index - Handles listing all todos and creating new ones
def index(request):
    todos = Todo.objects.all()      # Query function: Retrieve all Todo objects
    form = TodoForm()              # Form instantiation: Create a new TodoForm instance
    if request.method == 'POST':  # Conditional: Check if the request method is POST
        form = TodoForm(request.POST)  # Form instantiation: Create TodoForm with POST data
        if form.is_valid():       # Form validation: Check if the submitted data is valid
            form.save()           # Database operation: Save the new Todo object
            return redirect('index')  # Redirect function: Redirect to the index page
    return render(request, 'index.html', {'todos': todos, 'form': form})  # Render function: Display the index template
#RENDER: a user requests a web page, the server "renders" the content



# Function: update - Handles updating an existing todo
# Here, 'ck' is the parameter from the URL
# Todo.objects.get is a method
def update(request, ck):
    todo = Todo.objects.get(id=ck)      # Query function: Get a specific Todo object
    form = TodoForm(instance=todo)      # Form instantiation: Create TodoForm with existing Todo data
    if request.method == 'POST':        # Conditional: Check if the request method is POST
        form = TodoForm(request.POST, instance=todo)  # Form instantiation: Create TodoForm with POST data and existing Todo
        if form.is_valid():              # Form validation: Check if the submitted data is valid
            form.save()                  # Database operation: Save the updated Todo object
            return redirect('index')    # Redirect function: Redirect to the index page
    return render(request, 'update.html', {'form': form, 'todo': todo})  # Render function: Display the update template

# Function: delete - Handles deleting an existing todo
def delete(request, ck):
    todo = get_object_or_404(Todo, id=ck)        # Query function - Get a Todo object or raise 404 if not found
    if request.method == 'POST':                 # Conditional: Check if the request method is POST
        todo.delete()                            # Database operation: Delete the Todo object
        return redirect('index')                 # Redirect function: Redirect to the index page
    return render(request, 'delete.html', {'todo': todo})  # Render function: Display the delete template

def todo_list(request):
    todos = Todo.objects.all().order_by('-created_at')  # Get all todos, ordered by creation date
    return render(request, 'todo_list.html', {'todos': todos})

def search_todos(request):
    query = request.GET.get('query', '')
    todos = Todo.objects.filter(title__icontains=query).order_by('-created_at')
    return render(request, 'todo_list.html', {'todos': todos, 'query': query})

def complete_todo(request, ck):
    todo = get_object_or_404(Todo, id=ck)
    todo.completed = True
    todo.save()
    return redirect('todo_list')
