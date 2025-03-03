# quiz/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('save_topic', views.save_topic, name='save_topic'),  # URL for the quiz view
]