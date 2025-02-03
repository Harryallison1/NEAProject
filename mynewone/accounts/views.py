from django.shortcuts import render, redirect #Imports the render and redirect functions
from .forms import RegisterForm #Imports the custom RegisterForm class which I made myself

# Create your views here.

def register(request):
    print("Register view called") #used for debugging
    print(request.method) #used for debugging
    if request.method == 'POST':
        form = RegisterForm(request.POST) #if request is post then create instance of RegisterForm with data posted
        if form.is_valid():
            user = form.save()
            print(f"User {user.username} created successfully")
            print(user.password) #User object has no attribute "password1" or password2 however password worked but it is the encrypted version so we will not be able to display that to the user to tell them that they need to enter more characters i need to find the error which is raised when the user hasnt entered enough characters.
            return redirect("/introduction") #print user password also used for debugging
        else:
            print("form invalid") #debugging purposes
            print(form)

            if 'password1' in form.errors:
                # Get the error message for password1
                password_error = form.errors['password1']
                print(f"Password1 error: {password_error}")
            else:
                print("Password1 is valid, but there are other form errors.")

            # Optionally print the entire form errors for debugging
            print(form.errors)
            return render(request, "accounts/register.html", {"form": form })#Before this was not here neither were the if statements checking if the form was valid. Once i added this when the form was not valid it rdirected the user to the register template and in the template it loops through what the user has not done to successfully create an account
        #if the form is invalid it returns the same registration template with the form object
        #which now contains the user's inputs and the associated validation errors.
        #The render function renders the template and passes the form with errors back to the user.



        #redirect to a template telling them that an account has not been created and pass the form errors a
        #or redirect to the register template again and say how they need to do a new password.
            

       
            # Optionally, log the user in immediately after registration
            #user = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=user, password=raw_password)
            #if user is not None:
               # login(request, user)
                #return redirect('home')  # Redirect to a success page or home
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})     

#ur password can’t be too similar to your other personal information.

#How the code works on this page: I have saved it on a word document called Register View




       
