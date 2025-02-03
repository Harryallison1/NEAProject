from django import forms #Imports Django's form module to create and manage form fields
from django.contrib.auth import login, authenticate #Imports functions for logging in users and authenticating
from django.contrib.auth.forms import UserCreationForm #Imports forms for user registration, including validation
from django.contrib.auth.models import User #Imports user model which represents a user in Django's auth system

class RegisterForm(UserCreationForm): #Custom registration form extending UserCreationForm
    email = forms.EmailField() #Adds an additional email field to the registration form
    

    class Meta: #Defines metadata for the RegisterForm class
        model = User #Specifies that the form is based on the User model
        fields = ["username", "email", "password1", "password2"]     
        
        #Lists the fields from the user model and additional fields to include in the form
        #The reason we do not define the attributes of pass1 and pass2 and username is because
        #they are already inherited from UserCreationForm