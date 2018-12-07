from django.contrib import admin

from .models import *
# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
    list_display = ['thumb','name','name_slug']

admin.site.register(Pizza, PizzaAdmin)



