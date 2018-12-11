
from django import forms
from django.forms import ModelForm
from captcha.fields import CaptchaField
from shop.models import Testimonial
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class TestimonialForm(ModelForm):
    'Testimonial model form'
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit', 'Submit'))

    class Meta:
        model = Testimonial
        fields = ['email', 'name', 'message', 'captcha', 'pizza']
        widgets = {'pizza': forms.HiddenInput()}