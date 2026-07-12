import flet as ft

def main(page: ft.Page):
    page.title = "Exemplo Modal"
    
    # Este é um campo da tela principal que vai receber o valor de volta
    texto_principal = ft.Text("Nenhum inspetor identificado", size=18)

    # =========================================================================
    # A FUNÇÃO SOBREPOSTA (O NOSSO "FORM MODAL")
    # =========================================================================
    def abrir_captura_modal(e):
        
        # 1. Criamos o campo que vai capturar o dado DENTRO do pop-up
        campo_modal = ft.TextField(label="Digite o Número do Crachá", width=250)
        
        # 2. Função interna do botão "Confirmar" do pop-up
        def confirmar_e_fechar(e):
            # Passamos o valor capturado de volta para a tela de baixo!
            texto_principal.value = f"Inspetor Ativo: {campo_modal.value}"
            texto_principal.color = "blue"
            
            # Fechamos a janela sobreposta alterando a propriedade 'open' para False
            janela_modal.open = False
            page.update()

        # 3. Criamos a estrutura da Janela Flutuante (AlertDialog)
        janela_modal = ft.AlertDialog(
            modal=True, # Impede o usuário de fechar clicando fora da caixa
            title=ft.Text("Autenticação Requerida"),
            content=ft.Column([
                ft.Text("Para prosseguir, identifique-se:"),
                campo_modal
            ], tight=True), # 'tight=True' faz a caixinha se ajustar ao tamanho do conteúdo
            actions=[
                ft.ElevatedButton("Confirmar", on_click=confirmar_e_fechar),
                ft.TextButton("Cancelar", on_click=lambda _: setattr(janela_modal, "open", False) or page.update())
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )

        # 4. Injetamos o modal na página e mandamos abrir
        page.overlay.append(janela_modal)
        janela_modal.open = True
        page.update()
    # =========================================================================

    # Botão da tela de baixo que "chama" a função flutuante
    btn_chamar = ft.ElevatedButton("Iniciar Inspeção", on_click=abrir_captura_modal)

    # Adicionando na tela principal
    page.add(
        ft.Column([
            texto_principal,
            ft.Container(height=20),
            btn_chamar
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)
