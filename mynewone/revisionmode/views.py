from django.shortcuts import render #imports render, used to return an HTML response by rendering a template 

# Create your views here.


def save_topic(request):    
    selected_topic = None  #set to none originally, ensures variable is always defined even if a topic is not received

    if request.method == 'POST': #checks form is submitted 
        selected_topic = request.POST.get('topic', None) #extracts topic, looks for the key topic in POST request, assigned to NONE if not found
        if selected_topic:
            request.session['selected_topic'] = selected_topic #Stores topic in Django's session

    print(selected_topic)  #prints server side for debugging
    return render(request, 'mainmenu/mainmenu.html', {}) #renders mainmenu.html

