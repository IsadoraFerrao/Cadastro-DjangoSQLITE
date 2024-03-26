import pytest
from django.db.utils import IntegrityError
from cadastro.models import Cadastro

# Verificar se os valores foram salvos corretamente
@pytest.mark.django_db
def test_cadastro_criacao():
    
    # Criar uma instância da model Cadastro
    cadastro = Cadastro.objects.create(
        nome='Teste nome',
        email='teste@example.com',
        senha='testpassword123'
    )
    
    # Teste para verificar se os valores foram salvos corretamente
    assert cadastro.nome == 'Teste nome'
    assert cadastro.email == 'teste@example.com'
    assert cadastro.senha == 'testpassword123'
    
    # Testando a função str
    assert str(cadastro) == 'Teste nome: {} - teste@example.com'.format(cadastro.data)
    
    #Tentativa de criar um segundo cadastro com o mesmo email
    with pytest.raises(IntegrityError):
        Cadastro.objects.create(
            nome='Teste nome',
            email='teste@example.com',
            senha='testpassword123'
        )

    
