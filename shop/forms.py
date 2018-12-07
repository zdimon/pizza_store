
from django import forms


from django.forms import ModelForm
from account.models import Profile
from django.contrib.auth.models import User

class CustomerRegForm(ModelForm):
    'Profile registration model form'
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

'''
class RegForm(forms.Form):
    # simple form
    username = forms.CharField( label='Username', 
                                max_length=100,
                                widget= forms.TextInput(
                                    attrs={'class':'form-control'}
                                ))
    email = forms.EmailField(widget= forms.TextInput(
                                    attrs={'class':'form-control'}
                                ))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
'''