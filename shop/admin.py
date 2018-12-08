from django.contrib import admin

from .models import *
# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
    list_display = ['type','size','cost']

admin.site.register(Pizza, PizzaAdmin)

class PizzaTypeAdmin(admin.ModelAdmin):
    list_display = ['thumb','name','name_slug']

admin.site.register(PizzaType, PizzaTypeAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['email', 'message', 'is_public']

admin.site.register(Testimonial, TestimonialAdmin)