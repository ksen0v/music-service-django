import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
                    widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(
                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-input', 'required': 'required'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'required': 'required'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("This E-mail is already taken!")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username
    
class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['profile_photo', 'username', 'email', 'first_name']
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'profile_photo': forms.FileInput(attrs={'id': 'profile_photo'}),
        }