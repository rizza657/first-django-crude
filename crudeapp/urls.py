from django.urls import path  # Import the path function from django.urls
from . import views  # Import the views from the current directory
#parameters are variable that are defined in the fuction definition  
urlpatterns = [  # Define a list of URL patterns
    path('', views.index, name='index'),  # Root URL, maps to index view
    path('update/<int:ck>', views.update, name='update'),  # URL for updating, 'ck' is an integer parameter
    path('delete_todo/<int:ck>', views.delete, name='delete'),  # URL for deleting, 'ck' is an integer parameter
    path('todos/', views.todo_list, name='todo_list'),
    path('todos/search/', views.search_todos, name='search_todos'),
    path('complete/<int:todo_id>/', views.complete_todo, name='complete_todo'),    # New URL for todo list
    #int:ck'This allows you to easily retrieve the corresponding Todo object in your view using something like
]

#int:ck>  indicates that this is a name and integer parameter