from django.urls import path, include
from .views import detail, make_order, pay_order, pay_process, pay_success

urlpatterns = [
    path('detail/<str:slug>', detail, name="detail"),
    path('make_order/<int:pk>', make_order, name="make_order"),
    path('pay_order/<int:order_id>', pay_order, name="pay_order"),
    path('pay_success', pay_success, name="pay_success"),
    path('pay_process', pay_process, name="pay_process"),
]