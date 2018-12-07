from django.urls import path, include
from .views import login, logoutme, registration

urlpatterns = [
    path('login', login, name='login'),
    path('logout', logoutme, name='logout'),
    path('registration', registration, name='registration')
]