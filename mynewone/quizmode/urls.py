# quiz/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('quiz/', views.quiz_view, name='quiz'),  # URL for the quiz view
]
