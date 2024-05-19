from flet import *

def create_view(page: Page):
    return View(
        "/procurar",
        [
            AppBar(title=Text("Procurar", color='black'), bgcolor=colors.AMBER_700),
            # Adicione aqui os componentes da tela de procura
        ]
    )
