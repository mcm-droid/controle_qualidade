import flet as ft

def f_main(page: ft.Page):
    # 1. Configurações da página (título, alinhamento, etc.)
    page.title = "Minha Primeira Aula de Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 2. Criando os elementos visuais (Controls)
    texto = ft.Text(value="Olá, Mundo!", size=30, color="blue", weight=ft.FontWeight.BOLD)
    
    # 3. Adicionando os elementos na página
    page.add(texto)

# 4. Executando o aplicativo
ft.app(target=f_main)
