from django import forms
from libraryapp.models import Staff


class StaffForm(forms.ModelForm):
    SEXU = [
        ("Mane","Mane"),
        ("Feto","Feto"),
    ]

    sexu = forms.ChoiceField(choices=SEXU, widget=forms.Select(attrs={
        "class" : "form-control"
    }))

    class Meta:
        model = Staff
        exclude = ['id_staff']

    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        self.fields['naran_staff'].widget.attrs.update({
            "class":"form-control",
            "placeholder" : "Prense Naran Staff"
        })
        # self.fields['username'].widget.attrs.update({
        #     "class":"form-control",
        #     "placeholder" : "Prense Username"
        # })
        # self.fields['password'].widget.attrs.update({
        #     "class":"form-control",
        #     "placeholder" : "Prense Password"
        # })
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
        self.fields['username'].widget.attrs.update({
            "class":"form-control",
            "placeholder" : "Prense Username"
        })
        self.fields['password'].widget.attrs.update({
            "class":"form-control",
            "placeholder" : "Prense Password"
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
        self.fields['username'].required = False
        self.fields['password'].required = False
        self.fields['data_moris'].required = False
