from django import forms # type: ignore
from .models import Admin_user
from .models import Author

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

class AuthorForm(forms.ModelForm):

    SEXU_HILI = [
        ('M','Mane'),
        ('F', 'Feto')
    ]

    sexu = forms.ChoiceField(choices=SEXU_HILI, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Author
        fields = ['id_author', 'naran_author', 'sexu', 'email', 'nasaun']

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.fields['id_author'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'ID Author'
        })
        self.fields['naran_author'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Name Author'
        })
        self.fields['email'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Email'
        })
        self.fields['nasaun'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Nasaun'
        })
