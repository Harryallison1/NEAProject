from django.shortcuts import render, redirect

# Create your views here.



def main_menu(request):
    if request.method == 'POST':
        # Get the selected topic from the form submission
        topic = request.POST.get('topic')
        
        # Save the selected topic in the session
        request.session['selected_topic'] = topic
        return redirect('mainmenu')  # Redirect back to the main menu to avoid resubmission

    return render(request, 'mainmenu/mainmenu.html')