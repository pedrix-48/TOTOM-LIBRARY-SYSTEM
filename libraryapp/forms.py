from django import forms 
from .models import Admin_user, Author, Livru

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


class LivruForm(forms.ModelForm):

    TIPU_LIVRU = [
        ("Novel","Novel"), 
        ("Light Novel","Light Novel"), 
        ("Education", "Education"), 
        ("History", "History"), 
        ("Thesis","Thesis"),
        ("Children","Children"),
    ]
    tipu_livru = forms.ChoiceField(choices=TIPU_LIVRU, widget=forms.Select(attrs={'class': 'form-control'}))


    class Meta:
        model = Livru
        exclude = ['id_livru']

    def __init__(self, *args, **kwargs):
        super(LivruForm, self).__init__(*args, **kwargs)
        self.fields["titulu_livru"].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Prense Titulu Livru'
        })
        self.fields['data_publish'].widget = forms.DateInput(
            attrs={
                'class':'form-control',
                'placeholder':'Prense Data Publish',
                'type':'date'
            }
        )
        self.fields['nasaun'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Prense Nasaun'
        })
        self.fields['sypnosis'].widget.attrs.update({
            'class':'form-control',
            "id":"summernote_add"
        })
        self.fields['id_author'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['foto_livru'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Upload Cover Livru'
        })
