from django import forms

class InputForm(forms.Form):
    text = forms.CharField(label = "Enter your concerns here.",max_length=1500)
