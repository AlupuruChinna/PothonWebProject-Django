

from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.



def login(request):

    if request.method=='POST':
        user= auth.authenticate(username=request.POST['username'], password=request.POST['pwd1'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error' : 'Username or password is wrong'})

    return  render(request, 'login.html')

def signup(request):
    if request.method=='POST':
        try:
            if request.POST['pwd1'] == request.POST['pwd2']:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username has been taken already'})
            else:
                return render(request, 'signup.html', {'error': ' Password or username has mismatched'})
        except User.DoesNotExist:
            user= User.objects.create_user(username=request.POST['username'], password= request.POST['pwd1'])
            auth.login(request, user)
            return  render(request,'home.html',{'username' : request.POST['username']})
    return render(request, 'signup.html')


def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return  render(request,'home.html')