from django import forms
from .models import Admin_user

class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Admin_user
        fields = ['username', 'password']