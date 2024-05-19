from flet import *
import requests

def create_view(page: Page):
    API_URL = "http://127.0.0.1:5000/clientes"
    
    nome = TextField(label="Nome")
    documento = TextField(label="Documento (CPF ou RG)")
    email = TextField(label="Email")
    telefone = TextField(label="Telefone")
    celular = TextField(label="Celular")
    endereco = TextField(label="Endereço")
    observacao = TextField(label="Observação", multiline=True)
    
    response_text = Text()  # Adicionando um componente para exibir mensagens de resposta
    
    def enviar_dados(e):
        data = {
            "nome": nome.value,
            "documento": documento.value,
            "email": email.value,
            "telefone": telefone.value,
            "celular": celular.value,
            "endereco": endereco.value,
            "observacao": observacao.value
        }
        
        try:
            response = requests.post(API_URL, json=data)
            if response.status_code == 201:
                response_text.value = "Cliente cadastrado com sucesso!"
                response_text.color = colors.GREEN
            else:
                response_text.value = f"Erro ao cadastrar cliente: {response.status_code} - {response.text}"
                response_text.color = colors.RED
        except Exception as ex:
            response_text.value = f"Erro ao conectar com a API: {ex}"
            response_text.color = colors.RED
        
        page.update()
    
    enviar_button = ElevatedButton("Enviar", on_click=enviar_dados)
    
    return View(
        "/novo_cliente",
        [
            AppBar(title=Text("Cadastro de Clientes", color='black'), bgcolor=colors.AMBER_700),
            nome,
            documento,
            email,
            telefone,
            celular,
            endereco,
            observacao,
            enviar_button,
            response_text  # Adicionando o componente de resposta à página
        ]
    )