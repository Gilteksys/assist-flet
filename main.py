from flet import *
import nova_assistencia_tecnica
import novo_cliente
import nova_os
import procurar

def main(page: Page):
    page.title = "ASSIST-1.0"

    def mudanca_de_rota(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Cadastro", color='blue'), bgcolor=colors.AMBER_300),
                    ElevatedButton("Nova Assistência Técnica", on_click=lambda e: page.go("/nova_assistencia_tecnica")),
                    ElevatedButton("Novo Cliente", on_click=lambda e: page.go("/novo_cliente")),
                    ElevatedButton("Nova OS", on_click=lambda e: page.go("/nova_os")),
                    ElevatedButton("Procurar", on_click=lambda e: page.go("/procurar"))
                ]
            )
        )

        if page.route == "/nova_assistencia_tecnica":
            page.views.append(nova_assistencia_tecnica.create_view(page))
        elif page.route == "/novo_cliente":
            page.views.append(novo_cliente.create_view(page))
        elif page.route == "/nova_os":
            page.views.append(nova_os.create_view(page))
        elif page.route == "/procurar":
            page.views.append(procurar.create_view(page))

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = mudanca_de_rota
    page.on_view_pop = view_pop
    page.go(page.route)

API_URL = "http://127.0.0.1:5000/assistencias"

app(target=main, view=WEB_BROWSER)
