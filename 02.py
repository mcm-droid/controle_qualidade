import flet as ft

def main(page: ft.Page):
    page.title = "App Interativo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    texto = ft.Text(value="Clique no botão para ver a mágica...", size=20)

    # Função que será disparada pelo evento de clique
    def acao_do_botao(e):
        texto.value = "A mágica aconteceu! O texto mudou."
        texto.color = "green"
        # IMPORTANTE: Sempre que mudar uma propriedade de um controle já visível, 
        # você precisa dar um page.update() para renderizar a mudança.
        page.update()

    # Criando o botão e associando o evento 'on_click' à nossa função
    botao = ft.ElevatedButton(text="Clique Aqui", on_click=acao_do_botao)

    # Adicionando os dois elementos de uma vez
    page.add(texto, botao)

ft.app(target=main)
