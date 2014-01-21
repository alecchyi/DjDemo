'''
all forms
'''

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=50, widget = forms.PasswordInput)
    
    