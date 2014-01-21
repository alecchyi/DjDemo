'''
all forms
'''

from django import forms
from core.models import User

class LoginForm(forms.Form):
    
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    check_code = forms.CharField(max_length=4)
    
    def login(self):
        User.objects.create(self.username,self.password)
        
    
    