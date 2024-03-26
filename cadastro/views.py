from django.shortcuts import render, redirect
from django.http import HttpResponse 
from cadastro.forms import CadastroForm
from cadastro.models import Cadastro
# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def cadastro(request):
    sucesso = False 
    #if request.method == 'GET':
    form = CadastroForm(request.POST or None)
    if form.is_valid(): 
        sucesso = True
        form.save()
        return render(request, 'cadastro_logado.html', {'usuarios': Cadastro.objects.all()})
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'cadastro.html', contexto)