'''
all forms
'''

from django import forms
from core.models import Member, Blog

class LoginForm(forms.Form):
    
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget = forms.PasswordInput())
    check_code = forms.CharField(max_length=4)
    
    def login(self, request):
        if request.session.has_key("user_id") and request.session["user_id"] is not "":
            return 0
        try:
            member = Member.objects.get(username = self.cleaned_data["username"], 
                                        password = self.cleaned_data["password"])
        except Member.DoesNotExist:
            member = None
        if member is None:
            return 1
        else:
            request.session["user_id"] = member.id
            return 2
        
class BlogForm(forms.Form):
    
    title = forms.CharField(max_length=30, widget= forms.TextInput(attrs = {'class': 'blog_title'}))
    description = forms.CharField(max_length=500, widget = forms.Textarea())
    content = forms.CharField(max_length=2000, widget = forms.Textarea())
    
    def save(self, request):
        blog = {"title": self.cleaned_data["title"], 'content': self.cleaned_data["content"],
                'description': self.cleaned_data["description"], 'blog_type': 0, 'status': 1, 
                'member_id': request.session["user_id"]}
        Blog.objects.create(**blog)
        return 1
        
        
    
    