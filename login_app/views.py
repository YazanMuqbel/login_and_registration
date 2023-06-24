from django.shortcuts import render, redirect
from django.urls import reverse
from login_app.models import User
from django.contrib import messages

# Create your views here.
# This view takes the user to the home page where he can register or login
def home(request):
    return render(request,'homepage.html')

# this function handles data from the form and creates a new user, and also handle the first name + shows SUCCESS page.
def register(request):
    if request.method == 'POST':
        params = dict()
        
        params['first_name'] = request.POST.get('first_name')
        params['last_name'] = request.POST.get('last_name')
        params['email'] = request.POST.get('email')
        params['password'] = request.POST.get('password')
        params['confirm_password'] = request.POST.get('confirm_password')

        user = User.objects.create(**params)
        context = {
        'first_name': user.first_name
    }
        
        #**********************************************************
        errors = User.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('homepage')
    else:
        # redirect to a success route

        return render(request,'success.html', context)


        #**********************************************************
        


def success(request):
    return render(request,'success.html')

def error(request):
    return render(request,'error.html')

def logout(request):
    #request.session.clear()
    #return redirect("/")
    #return redirect('homepage')
    return render(request,'logout.html')

def login(request):
    return render(request,'success.html')