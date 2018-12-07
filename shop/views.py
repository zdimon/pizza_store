from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Create your views here.
from django.contrib import messages

from .forms import CustomerRegForm as RegForm
from .lib.shop_class import Shop
from .models.pizza import Pizza

def home(request):
    form = RegForm()
    shop = Shop()
    pizzas = Pizza.objects.all()

    return render(request,'shop/home.html', {'shop': shop, 'form': form, 'pizzas': pizzas})

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
    
