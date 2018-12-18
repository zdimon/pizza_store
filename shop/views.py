from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.contrib import messages

from account.forms import CustomerRegForm as RegForm
from .lib.shop_class import Shop
from .models import PizzaType
from .models import Order
from .models import Testimonial
from django.http import Http404, HttpResponse
from .forms import TestimonialForm
from django.views.generic.edit import FormView
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)
response = HttpResponse()

def home(request):
    
    logger.info('Something went wrong!')
    print(request.session.get('_auth_user_id'))
    form = RegForm()
    shop = Shop()
    pizzas = PizzaType.objects.all()
    response = render(request,'shop/home.html', {'shop': shop, 'form': form, 'pizzas': pizzas})
    response.set_cookie('cookie_name', 'cookie_value')
    return response
    

def detail(request,slug):
    try:
        pizza = PizzaType.objects.get(name_slug=slug)
    except:
        raise Http404('Не смог найти пицку %s' % slug)
    tm = Testimonial()
    tm.pizza = pizza
 
    if request.method == 'POST':
        tform = TestimonialForm(request.POST, request.FILES)
        if tform.is_valid():  
            tform.save()
            messages.success(request, 'Thank you!')
            tform = TestimonialForm(instance=tm)
    else:
        tform = TestimonialForm(instance=tm)


    return render(request,'shop/detail.html',{'pizza': pizza, 'tform': tform})

def make_order(request,pk):
    pizza_type = get_object_or_404(PizzaType,pk=pk)
    orders = Order.objects.all()
    o = Order.objects.create(pizza=pizza_type)
    #pizza_type.make_order(request)
    return render(request,'shop/order_list.html',{'pizza': pizza_type, 'orders': orders})




