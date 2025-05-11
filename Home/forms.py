from django import forms

class usersForm(forms.Form):
    username=forms.CharField(label='value 1',required=False, widget=forms.TextInput(attrs={'class':"form-control"}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control"}))
    password=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))