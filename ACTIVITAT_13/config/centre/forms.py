from django import forms
from .models import Alumne, Professor


class alumneForm(forms.ModelForm):
        class Meta:
            model = Alumne
            fields = '__all__'


class professorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'