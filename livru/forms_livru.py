from django import forms

from libraryapp.models import Livru


class LivruForm(forms.ModelForm):
    

    TIPU_LIVRU = [
        ("Novel","Novel"), 
        ("Light Novel","Light Novel"), 
        ("Manga","Manga"), 
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
            "id":"summernote"
        })
        self.fields['id_author'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['foto_livru'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Upload Cover Livru'
        })

class EditInfoDetailLivru(forms.ModelForm):
    TIPU_LIVRU = [
        ("Novel","Novel"), 
        ("Light Novel","Light Novel"), 
        ("Manga","Manga"), 
        ("Education", "Education"), 
        ("History", "History"), 
        ("Thesis","Thesis"),
        ("Children","Children"),
    ]
    tipu_livru = forms.ChoiceField(choices=TIPU_LIVRU, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Livru
        fields = [
            "tipu_livru",
            "titulu_livru",
            "data_publish",
            "nasaun",
            "id_author"
        ]
    def __init__(self, *args, **kwargs):
        super(EditInfoDetailLivru, self).__init__(*args, **kwargs)
        self.fields['titulu_livru'].widget.attrs.update({
            "class" : "form-control",
            "placeholder" : "Prense Titulu Livru",
        })
        self.fields['nasaun'].widget.attrs.update({
            "class" : "form-control",
            "placeholder" : "Prense Nasaun",
        })
        self.fields['id_author'].widget.attrs.update({
            "class" : "form-control",
        })
        self.fields['data_publish'].widget = forms.DateInput(
            attrs={
                'class':'form-control',
                'placeholder':'Prense Data Publisidade',
                'type':'date'
            }
        )
        self.fields["nasaun"].required = False
        self.fields["id_author"].required = True
        self.fields["data_publish"].required = False
        self.fields["tipu_livru"].required = False

class EditSypnosisLivruForm(forms.ModelForm):
    class Meta:
        model = Livru
        fields = ['sypnosis']

    def  __init__(self, *args, **kwargs):
        super(EditSypnosisLivruForm, self).__init__(*args, **kwargs)
        self.fields['sypnosis'].widget.attrs.update({
            "class" : "form-control",
            "id" : "summernote_add"
        })
        self.fields['sypnosis'].required = False
