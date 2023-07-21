from django import forms
from .models import Morador

class MoradorForm(forms.ModelForm):
    class Meta:
        model = Morador
        fields = '__all__'