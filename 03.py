import flet as ft

# Uma função dedicada exclusivamente a fabricar o Cabeçalho (Header)
def criar_header_sistema():
    return ft.Container(
        content=ft.Text("SISTEMA DE CONTROLE DE QUALIDADE", color="white"),
        bgcolor="blue",
        padding=20
    )

# Uma função dedicada exclusivamente a fabricar o Formulário
def criar_formulario_cadastro(page):
    txt_input = ft.TextField(label="Código do Lote")
    
    def acao_salvar(e):
        # A lógica fica guardadinha aqui dentro, escondida de quem monta a tela
        print(f"Lote {txt_input.value} verificado.")
        
    btn_salvar = ft.ElevatedButton("Validar", on_click=acao_salvar)
    
    return ft.Column([txt_input, btn_salvar])


# O MAIN vira apenas um "Gerente de Montagem" super limpo e elegante:
def main(page: ft.Page):
    page.title = "Controle de Qualidade"
    
    # Montagem cirúrgica: chama as funções construtoras
    header = criar_header_sistema()
    formulario = criar_formulario_cadastro(page)
    
    # Adiciona no palco principal
    page.add(header, formulario)

ft.app(target=main)
