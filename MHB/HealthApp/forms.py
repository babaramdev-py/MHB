from django import forms

class InputForm(forms.Form):
    text = forms.CharField(label = "",max_length=1500, widget=forms.Textarea)
