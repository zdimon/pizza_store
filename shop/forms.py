
from django import forms
from django.forms import ModelForm
from captcha.fields import CaptchaField
from shop.models import Testimonial

class TestimonialForm(ModelForm):
    'Testimonial model form'
    captcha = CaptchaField()
    class Meta:
        model = Testimonial
        fields = ['email', 'name', 'message', 'captcha']