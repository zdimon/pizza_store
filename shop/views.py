from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.contrib import messages

from account.forms import CustomerRegForm as RegForm
from .lib.shop_class import Shop
from .models import Pizza
from .models import Order
from django.http import Http404
from .forms import TestimonialForm

def home(request):
    form = RegForm()
    shop = Shop()
    pizzas = Pizza.objects.all()
    return render(request,'shop/home.html', {'shop': shop, 'form': form, 'pizzas': pizzas})




    

def detail(request,slug):
    try:
        pizza = Pizza.objects.get(name_slug=slug)
    except:
        raise Http404('Не смог найти пицку %s' % slug)

    tform = TestimonialForm()
    return render(request,'shop/detail.html',{'pizza': pizza, 'tform': tform})

def make_order(request,pk):
    pizza = get_object_or_404(Pizza,pk=pk)
    orders = Order.objects.all()
    pizza.make_order(request)
    return render(request,'shop/order_list.html',{'pizza': pizza, 'orders': orders})