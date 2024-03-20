from django import forms 
from cadastro.models import Cadastro
class CadastroForm(forms.Form):
    class Meta:
        model = Cadastro
        fields = ['nome', 'email', 'senha']
        