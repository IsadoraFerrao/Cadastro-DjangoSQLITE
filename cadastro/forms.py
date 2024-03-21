from django import forms 
from cadastro.models import Cadastro

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ['nome', 'email', 'senha']
    senha = forms.CharField(widget=forms.PasswordInput)