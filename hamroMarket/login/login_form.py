from django import forms  
from login.models import Login 
  
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:  
        model = Login
        fields = "__all__" 
        labels = {
            'username': 'Username',
            'password': 'Password'
        }

        #selecting some fields
        #fields = ('first_name', 'last_name',)