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
        fields = ['naran_author', 'sexu', 'data_moris','email', 'nasaun', 'deskrisaun','foto_profile']

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.fields['naran_author'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Prense Naran Autor'
        })
        self.fields['data_moris'].widget = forms.DateInput(
            attrs={
                'class':'form-control',
                'placeholder':'Prense Data Moris',
                'type':'date'
            }
        )
        self.fields['email'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Prense Email',
            'type':'email'
        })
        self.fields['nasaun'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Prense Nasaun'
        })
        self.fields['deskrisaun'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Prense Deskrisaun',
            'id':'summernote_add',
        })
        self.fields['foto_profile'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Upload Foto Profile'
        })
