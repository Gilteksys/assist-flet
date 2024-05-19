from flet import *
import requests

def create_view(page: Page):
    API_URL = "http://127.0.0.1:5000/assistencias"
    
    razao_social = TextField(label="Razão Social")
    nome_fantasia = TextField(label="Nome Fantasia")
    cnpj = TextField(label="CNPJ")
    inscricao_estadual = TextField(label="Inscrição Estadual")
    email = TextField(label="Email")
    telefone = TextField(label="Telefone")
    celular = TextField(label="Celular")
    endereco = TextField(label="Endereço")
    observacao = TextField(label="Observação", multiline=True)
    
    response_text = Text()  # Adicionando um componente para exibir mensagens de resposta
    
    def enviar_dados(e):
        data = {
            "razao_social": razao_social.value,
            "nome_fantasia": nome_fantasia.value,
            "cnpj": cnpj.value,
            "inscricao_estadual": inscricao_estadual.value,
            "email": email.value,
            "telefone": telefone.value,
            "celular": celular.value,
            "endereco": endereco.value,
            "observacao": observacao.value
        }
        
        try:
            response = requests.post(API_URL, json=data)
            if response.status_code == 201:
                response_text.value = "Assistência Técnica cadastrada com sucesso!"
                response_text.color = colors.GREEN
            else:
                response_text.value = f"Erro ao cadastrar Assistência Técnica: {response.status_code} - {response.text}"
                response_text.color = colors.RED
        except Exception as ex:
            response_text.value = f"Erro ao conectar com a API: {ex}"
            response_text.color = colors.RED
        
        page.update()
    
    enviar_button = ElevatedButton("Enviar", on_click=enviar_dados)
    
    return View(
        "/nova_assistencia_tecnica",
        [
            AppBar(title=Text("Nova Assistência Técnica", color='black'), bgcolor=colors.AMBER_700),
            razao_social,
            nome_fantasia,
            cnpj,
            inscricao_estadual,
            email,
            telefone,
            celular,
            endereco,
            observacao,
            enviar_button,
            response_text  # Adicionando o componente de resposta à página
        ]
    )
