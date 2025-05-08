from django import forms
from libraryapp.models import Staff


class AddStaffForm(forms.ModelForm):
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
        super(AddStaffForm, self).__init__(*args, **kwargs)
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
        self.fields['email'].required = False
