from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("welcome")
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def register(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Taken')
            return redirect('register')

        else:
            user = User.objects.create_user(username = username, password = password, email = email)
            user.save();
            print('user created') 
            return redirect('login')

    else:
        return render(request, 'register.html')

    return redirect("/")

def logout(request):
    auth.logout(request)
    return redirect ("/")


def portfolio(request):
    return render(request, "portfolio.html")


def welcome(request):
    return render(request, "welcome.html")

def appointment(request):
    return render(request, "appointment.html")

def beautify(request):
    return render(request, "beautify.html")