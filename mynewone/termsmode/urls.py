from django.urls import path
from . import views

urlpatterns = [
    path('terms/', views.terms_view, name='terms'), 
]