from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

class InputForm(forms.Form):
    text = forms.CharField(label = "",max_length=1500, widget=forms.Textarea(attrs={'class':'form-group'}))



class LoginForm(AuthenticationForm):
    pass

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    concerns = forms.CharField(max_length=256, required=True)

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2', 'concerns']

