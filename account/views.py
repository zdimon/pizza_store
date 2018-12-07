from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as l

def login(request):
    username = request.POST['login']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        l(request, user)
        return redirect('home')
    else:
        messages.warning(request, 'Error!!!!')
        return redirect('home')

def logoutme(request):
    logout(request)
    return redirect('home')

def registration(request):
 if request.method == 'POST':
    # create a form instance and populate it with data from the request:
    form = RegForm(request.POST)
    # check whether it's valid:
    if form.is_valid():  
        form.save()
        messages.success(request, 'Bingo !!!')
        return redirect('home')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
