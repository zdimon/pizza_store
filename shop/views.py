from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
# Create your views here.
from django.contrib import messages

from .forms import CustomerRegForm as RegForm
from .lib.shop_class import Shop
from .models.pizza import Pizza
from .models.order import Order
from django.http import Http404

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
    

def detail(request,slug):
    try:
        pizza = Pizza.objects.get(name_slug=slug)
    except:
        raise Http404('Не смог найти пицку %s' % slug)

    return render(request,'shop/detail.html',{'pizza': pizza})

def make_order(request,pk):
    pizza = get_object_or_404(Pizza,pk=pk)
    orders = Order.objects.all()
    pizza.make_order(request)
    return render(request,'shop/order_list.html',{'pizza': pizza, 'orders': orders})