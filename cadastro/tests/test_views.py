import pytest 
from django.urls import reverse
from django.test import RequestFactory
from cadastro.views import cadastro 

@pytest.mark.django_db
def test_cadastro_view():
    # Criar uma instância do RequestFactory
    factory = RequestFactory()
    
    #Define os dados para o formulário
    data = {
        'name': 'Test User',
        'email': 'test@example.com' 
    }
    
    #Cria uma requisição POST com os dados do formulário
    request = factory.post(reverse('cadastro'), data)
    response = cadastro(request)
    
    #Verificações
    assert response.status_code == 200