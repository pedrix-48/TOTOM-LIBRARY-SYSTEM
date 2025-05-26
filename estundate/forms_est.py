from libraryapp.models import Estudante
from django import forms


class AddEstudanteForm(forms.ModelForm):
    SEXU  = (
        ('Mane', 'Mane'),
        ('Feto', 'Feto'),
    )
    
    sexu = forms.ChoiceField(choices=SEXU, widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Estudante
        fields  = "__all__"
        
        
    def __init__(self, *args, **kwargs):
        super(AddEstudanteForm, self).__init__(*args, **kwargs)
        self.fields['nre'].widget.attrs.update({
            'class' : "form-control",
            "placeholder": "Prense NRE"
        })
        self.fields['naran_estudante'].widget.attrs.update({
            'class' : "form-control",
            "placeholder": "Prense Naran Estudante"
        })
        self.fields['id_dep'].widget.attrs.update({
            'class' : "form-control",
            "placeholder": "Prense Departamento"
        })
        self.fields['periodo'].widget.attrs.update({
            'class' : "form-control",
            "placeholder": "Prense Tinan"
        })
        self.fields['nu_telefone'].widget.attrs.update({
            'class' : "form-control",
            "placeholder": "Prense Numeru Telefone"
        })
        self.fields['data_moris'].widget = forms.DateInput(
            attrs={
                'class': "form-control",
                'placeholder': "Prense Data Moris",
                'type': 'date'
            },
            format='%d-%m-%Y'
        )
        self.fields['email'].widget.attrs.update({
            'class' : "form-control",
            "placeholder": "Prense Email"
        })
        self.fields['hela_fatin'].widget.attrs.update({
            'class' : "form-control",
            "placeholder": "Prense Hela Fatin"
        })
        self.fields['foto_profile'].widget.attrs.update({
            'class' : "form-control",
            "placeholder": "Hili Foto Profile",
        })