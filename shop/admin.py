from django.contrib import admin

from .models import *
# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name','thumb', 'name_slug']
    readonly_fields = ["name_slug"]

admin.site.register(Pizza, PizzaAdmin)



