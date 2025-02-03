from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('progress/', views.progress_view, name='progress'),
    path('about/', views.about, name='about'),
]

#url patterns is a list where you define the url patterns for your app
#Each entry in the list maps a specific url path to a view function
#' ' empty string means that this pattern matches the root URL for this app
#views.index this points to the index function in the views.py file. When a user visits this url the index view
#function is called to handle the request
#name='index' Optional name you can give to url pattern, allows you to reference in templates





#path('progress/', views.progress_view, name='progress'),