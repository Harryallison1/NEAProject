from django.urls import path
from .views import main_menu

urlpatterns = [
    path('mainmenu/', main_menu, name='main_menu'),
]
