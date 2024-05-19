from flet import *
import requests
from datetime import datetime

def create_view(page: Page):
    API_URL = "http://127.0.0.1:5000/oficinas"
    
    aparelho = TextField(label="Aparelho")
    marca = TextField(label="Marca")
    modelo = TextField(label="Modelo")
    numero_serie = TextField(label="Número de Série")
    data_entrada = TextField(label="Data de Entrada", hint_text="DD/MM/YYYY")
    data_saida = TextField(label="Data de Saída", hint_text="DD/MM/YYYY")
    garantia = TextField(label="Garantia")
    observacao = TextField(label="Observação", multiline=True)
    cliente_id = TextField(label="ID do Cliente")
    
    response_text = Text()
    
    def enviar_dados(e):
        # Convertendo as datas para o formato esperado pela API
        data_entrada_value = datetime.strptime(data_entrada.value, '%d/%m/%Y').date()
        data_saida_value = datetime.strptime(data_saida.value, '%d/%m/%Y').date()

        data = {
            "aparelho": aparelho.value,
            "marca": marca.value,
            "modelo": modelo.value,
            "numero_serie": numero_serie.value,
            "data_entrada": data_entrada_value.strftime('%Y/%m/%d'),
            "data_saida": data_saida_value.strftime('%Y/%m/%d'),
            "garantia": garantia.value,
            "observacao": observacao.value,
            "cliente_id": cliente_id.value
        }
        
        # Adiciona logs de debug
        #print("Dados enviados:", data)
        
        try:
            response = requests.post(API_URL, json=data)
            print("Resposta da API:", response.status_code, response.text)
            if response.status_code == 201:
                response_text.value = "OS cadastrada com sucesso!"
                response_text.color = colors.GREEN
            else:
                response_text.value = f"Erro ao cadastrar OS: {response.status_code} - {response.text}"
                response_text.color = colors.RED
        except Exception as ex:
            response_text.value = f"Erro ao conectar com a API: {ex}"
            response_text.color = colors.RED
        
        page.update()
    
    enviar_button = ElevatedButton("Enviar", on_click=enviar_dados)
    
    return View(
        "/nova_os",
        [
            AppBar(title=Text("Nova OS", color='black'), bgcolor=colors.AMBER_700),
            aparelho,
            marca,
            modelo,
            numero_serie,
            data_entrada,
            data_saida,
            garantia,
            observacao,
            cliente_id,
            enviar_button,
            response_text
        ]
    )





