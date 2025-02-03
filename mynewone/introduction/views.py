from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, "introduction/base.html", {})

def about(request):
    return render(request, "introduction/about.html", {})

#index view function. When it receives a user request it will render the base html template which contains 
#the home page

def progress_view(request):
    # Example: Replace with real data
    progress_data = {
        'username': 'John Doe',
        'completed_tasks': 5,
        'total_tasks': 10,
        'progress_percentage': 50
    }
    return render(request, 'introduction/progress.html', progress_data)