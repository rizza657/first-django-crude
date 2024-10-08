"""
URL configuration for crudeui project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#collection of related functions, classes, and variables that can be imported and used in other code.
#This is a module within Django that contains various applications
from django.contrib import admin #The contrib module includes several built-in features like authentication, sessions, and the admin interface.



#parameters are variable that are defined in the fuction definition  
#This module in Django that provides utilities for URL handling and routing within your web application.


from django.urls import path, include #include --- to include another URLconf, allowing for modular URL routing. 
# This is useful for organizing URLs across multiple apps.

urlpatterns = [      #<-- li
    path('admin/', admin.site.urls), #T URL configurations provided by Django's admin module, which handles the routing of requests to the appropriate views for managing the application's data.
    path('', include('crudeapp.urls'))
]
