from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User

class UserLoginForm(AuthenticationForm):
    
    username = forms.CharField()
    password = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'password']
        
        
class UserRegisterForm(UserCreationForm):
    
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class ProfileForm(UserChangeForm):
    
    username = forms.CharField()
    email = forms.CharField()
    image = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'image', 'email']