from django import forms
from libraryapp.models import Staff
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm


class StaffForm(forms.ModelForm):
    SEXU = [
        ("Mane","Mane"),
        ("Feto","Feto"),
    ]

    username = forms.CharField(max_length=255, required=False)
    password = forms.PasswordInput()

    sexu = forms.ChoiceField(choices=SEXU, widget=forms.Select(attrs={
        "class" : "form-control"
    }))

    class Meta:
        model = Staff
        fields = [
            'naran_staff',
            'username',
            # 'password',
            'nu_telefone',
            'email',
            'hela_fatin',
            'foto_staff',
            'data_moris',
            'sexu',

        ]

    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        self.fields['naran_staff'].widget.attrs.update({
            "class":"form-control",
            "placeholder" : "Prense Naran Staff"
        })
        self.fields['username'].widget.attrs.update({
            "class":"form-control",
            "placeholder" : "Prense Username"
        })
        self.fields['nu_telefone'].widget.attrs.update({
            "class":"form-control",
            "placeholder" : "Prense Numeru Telemovel"
        })
        self.fields['email'].widget.attrs.update({
            "class":"form-control",
            "placeholder" : "Prense Email",
            "type" : "email"
        })
        self.fields['hela_fatin'].widget.attrs.update({
            "class":"form-control",
            "placeholder" : "Prense Hela Fatin",
        })
        self.fields['foto_staff'].widget.attrs.update({
            "class":"form-control",
            "placeholder" : "Prense Hela Fatin",
        })
        self.fields["data_moris"].widget = forms.DateTimeInput(
            attrs={
                'class' : 'form-control',
                "placeholder" : "Prense Data Moris",
                "type" : "date"
            }
        )
        self.fields['email'].required = False
        self.fields['nu_telefone'].required = False
        

class EditDetallaFormStaff(forms.ModelForm):
    SEXU = [
        ("Mane","Mane"),
        ("Feto","Feto"),
    ]

    sexu = forms.ChoiceField(choices=SEXU, widget=forms.Select(attrs={
        "class" : "form-control"
    }))

    class Meta:
        model = Staff
        exclude = ['foto_staff', 'id_staff']

    def __init__(self, *args, **kwargs):
        super(EditDetallaFormStaff, self).__init__(*args, **kwargs)
        self.fields['naran_staff'].widget.attrs.update({
            "class":"form-control",
            "placeholder" : "Prense Naran Staff"
        })
        self.fields['nu_telefone'].widget.attrs.update({
            "class":"form-control",
            "placeholder" : "Prense Numeru Telemovel"
        })
        self.fields['email'].widget.attrs.update({
            "class":"form-control",
            "placeholder" : "Prense Email",
            "type" : "email"
        })
        self.fields['hela_fatin'].widget.attrs.update({
            "class":"form-control",
            "placeholder" : "Prense Hela Fatin",
        })
        self.fields["data_moris"].widget = forms.DateTimeInput(
            attrs={
                'class' : 'form-control',
                "placeholder" : "Prense Data Moris",
                "type" : "date"
            }
        )
        self.fields['sexu'].required = False
        self.fields['hela_fatin'].required = False
        self.fields['email'].required = False
        self.fields['nu_telefone'].required = False
        self.fields['data_moris'].required = False

class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({"class" : "form-control", "placeholder" : "Prense Username"})
        
class BootstrapPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label
            })
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Prense Username"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Prense Password"
        })
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
    
    
