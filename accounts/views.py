from django.shortcuts import render, redirect
#from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def signupView(request):
    return render(request, 'signup.html')

def signupController(request):
    if(request.method == 'POST'):
        firstName = request.POST['firstname']
        lastName = request.POST['lastname']
        userName = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmpassword']

        if password == confirmPassword:
            if(User.objects.filter(username=userName).exists()):
                messages.info(request, "UserName already exists")
                return redirect("signup")
                
            elif(User.objects.filter(email=email).exists()):
                messages.info(request, "Email already exists")
                return redirect("signup")

            else:
                #user = get_user_model().objects.create_user(first_name=firstName, last_name=lastName, username=userName, email=email, password=password)
                user = User.objects.create_user(first_name=firstName, last_name=lastName, username=userName, email=email, password=password)
                user.save()
                return redirect("signup")

        else:
            messages.info(request, "Password does not match")
            return redirect("signup")
        
    else:
        return render(request, 'signup.html')

def loginView(request):
    return render(request, 'login.html')

def loginController(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if(user is not None):
            auth.login(request, user)
            return redirect('/')
        
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('loginView')
        
def logoutController(request):
    auth.logout(request)
    return redirect('/')