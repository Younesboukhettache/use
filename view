from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import trol


# Create your views here.

def younes(request):

    return render(request, 'home.html', {'up':trol.objects.all()})


    
    


def new(request):


    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        data = User.objects.create_user(username=username, email=email, password=password)
        
        data.save()
        
        return redirect('enter')

    return render(request, 'new.html')
    

def dkhal(request,):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        data = authenticate(username=username, password=password)
        if data is not None:
            login(request, data)
            return redirect('home')
        else:
            messages.info(request, 'the username or the password is faulse ')
            return redirect('enter')
            

    return render(request, 'enter.html',)


def out(request):
    
    logout(request)
    return render(request, 'out.html')


    

def post(request):


    if request.method == 'POST':
        sharing = request.POST['sharing']
        
        data = trol.objects.create_by(sharing=sharing)
        data.save()
        return redirect('home')
    return render(request, 'post.html')









    




    
