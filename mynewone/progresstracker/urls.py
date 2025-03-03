from django.urls import path
from . import views

urlpatterns = [
    path('userprogress/', views.progress_view, name='userprogress'),  # URL for the quiz view
]