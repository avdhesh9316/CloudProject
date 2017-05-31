from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm
# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)  # grabbing the user form data in user_form variable
        profile_form = UserProfileInfoForm(data=request.POST)  # Grabbing the profile form in profile_form
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()    # saving the user form to the databse
            user.set_password(user.password)  # Hashing the password
            user.save()   # save the hash password to the database
            profile = profile_form.save(commit=False) # We are not saving the profile form to the databse yet. This is bcoz with the conflicting with user form
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm() # if the request is not a POST request then we just create an instance of class UserForm() instead of invalidating and saving it to further
        profile_form = UserProfileInfoForm()  #Similer instance of class UserProfileInfoForm
    return render(request,'basic_app/registration.html',{'user_form':user_form,'profile_form':profile_form,
                'registered':registered}) # passing context dictnory variable referenced in registration.html file
