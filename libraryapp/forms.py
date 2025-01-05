from django import forms
from .models import Admin_user

class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Admin_user
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(AdminLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Username'
        })
        self.fields['password'].widget = forms.PasswordInput({
            'class':'form-control',
            'placeholder':'Password'
        })