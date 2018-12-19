from django.urls import path, include
from .views import detail, make_order

urlpatterns = [
    path('detail/<str:slug>', detail, name="detail"),
    path('make_order/<int:pk>', make_order, name="make_order")
]
