import flet as ft

# Configuração de Cores e Estilo do Sistema (Design System)
TEMA = {"PRIMARIA": "#1E3A8A",       # Azul Escuro Profissional
        "SECUNDARIA": "#3B82F6",     # Azul Claro/Destaque
        "FUNDO_CARD": "#F3F4F6",     # Cinza Claro para os botões/cards
        "TEXTO_ESCURO": "#1F2937",   # Cinza Quase Preto para leitura
        "TEXTO_CLARO": "#FFFFFF",    # Branco para o cabeçalho
        "HOVER": "#E5E7EB"}           # Cinza um pouco mais escuro para o efeito de passar o mouse

# Árvore de Navegação (A Estrutura de Menus do FoxPro, mapeada em Dicionário Python)
ESTRUTURA_MENUS = {
    "Menu Principal": {
        "1. Controle de Processos": {
            "1.1. Inspeção de Linha": None,
            "1.2. Registro de Não Conformidade": None,
            "1.3. Liberação de Lote": None,
            "Voltar": "VOLTAR"
        },
        "2. Gestão de Indicadores (KPIs)": {
            "2.1. Gráficos de Desempenho": None,
            "2.2. Relatório de Desperdício": None,
            "Voltar": "VOLTAR"
        },
        "3. Auditoria e Normas": {
            "3.1. Checklist ISO 9001": None,
            "3.2. Histórico de Auditorias": None,
            "Voltar": "VOLTAR"
        },
        "Sair do Sistema": "SAIR"
    }
}

# ==========================================
# SUBFUNÇÃO: Especialista em desenhar o Topo
# ==========================================
def criar_header_sistema(tema,icone,titulo,cor_texto,cor_fundo):
    return ft.Container(
        content=ft.Row([ft.Icon(icone, color=cor_texto, size=30),
                        ft.Text(titulo,size=22,weight=ft.FontWeight.BOLD,color=cor_texto)],
                        alignment=ft.MainAxisAlignment.CENTER),bgcolor=cor_fundo,padding=ft.padding.symmetric(vertical=20, horizontal=10),alignment=ft.alignment.center,)   

# ==========================================
# FUNÇÃO PRINCIPAL: Onde a mágica acontece
# ==========================================
def main(page: ft.Page):
    page.title = "Controle de Qualidade v2.0"
    page.window_width = 650
    page.window_height = 700
    page.window_resizable = False
    
    # Lista que guarda onde o usuário está (Ex: ["Menu Principal", "1. Controle de Processos"])
    historico_navegacao = ["Menu Principal"]

    # Função auxiliar para descobrir em qual parte do dicionário estamos
    def obter_menu_atual():
        menu_auxiliar = ESTRUTURA_MENUS
        # Navega pelo dicionário seguindo os passos do histórico (pulando o primeiro que é o nó raiz)
        for passo in historico_navegacao[1:]:
            menu_auxiliar = menu_auxiliar[passo]
        return menu_auxiliar

    # Função que redesenha a tela de opções dinamicamente
    def atualizar_painel_visual():
        # 1. Atualizar a linha de caminhos (Breadcrumbs)
        linha_caminho.controls.clear()
        for i, passo in enumerate(historico_navegacao):
            if i > 0:
                linha_caminho.controls.append(ft.Text(">", color=TEMA["SECUNDARIA"], size=16, weight=ft.FontWeight.BOLD))
            
            # Torna o caminho clicável para o usuário poder voltar direto por ele
            linha_caminho.controls.append(
                ft.TextButton(
                    content=ft.Text(passo, color=TEMA["PRIMARIA"], weight=ft.FontWeight.W_600),
                    on_click=lambda e, p=passo: clicar_no_caminho(p)
                )
            )

        # 2. Atualizar os botões do Menu
        painel_opcoes.controls.clear()
        menu_atual = obter_menu_atual()

        for opcao, subconteudo in menu_atual.items():
            
            # Função interna para gerenciar o clique de cada botão criado
            def ao_clicar_opcao(e, opt=opcao, sub=subconteudo):
                if sub == "SAIR":
                    page.window.close()
                elif sub == "VOLTAR" or opt == "Voltar":
                    if len(historico_navegacao) > 1:
                        historico_navegacao.pop()
                        atualizar_painel_visual()
                elif isinstance(sub, dict):
                    # Se o subconteúdo for outro dicionário, significa que é um SUBMENU!
                    historico_navegacao.append(opt)
                    atualizar_painel_visual()
                else:
                    # Se for None, significa que clicamos numa tela final de formulário/rotina!
                    exibir_tela_final(opt)

            # Efeito visual de iluminar o botão ao passar o mouse (Hover)
            # 1. Uma única função de Hover muito mais inteligente:
            def efeito_hover_botao(e):
                # e.data == "true" significa que o mouse ENTROU
                # e.data == "false" significa que o mouse SAIU
                e.control.bgcolor = TEMA["HOVER"] if e.data == "true" else TEMA["FUNDO_CARD"]
                e.control.update() # Força o botão específico a se redesenhar

            # 2. Na hora de criar o botão (ft.Container), amarre a função acima:
            botao_opcao = ft.Container(
                content=ft.Row([
                    ft.Icon(ft.Icons.ARROW_FORWARD_IOS_ROUNDED, size=16, color=TEMA["SECUNDARIA"]),
                    ft.Text(opcao, size=16, weight=ft.FontWeight.W_500, color=TEMA["TEXTO_ESCURO"])
                ], alignment=ft.MainAxisAlignment.START),
                padding=ft.padding.symmetric(vertical=15, horizontal=20),
                bgcolor=TEMA["FUNDO_CARD"],
                border_radius=8,
                on_click=ao_clicar_opcao,
                on_hover=efeito_hover_botao # <-- Mudamos para a nossa nova função unificada!
            )
            painel_opcoes.controls.append(botao_opcao)
            
        area_conteudo.controls.clear()
        area_conteudo.controls.append(painel_opcoes)
        page.update()

    def clicar_no_caminho(passo_clicado):
        # Corta o histórico até o ponto onde o usuário clicou
        if passo_clicado in historico_navegacao:
            indice = historico_navegacao.index(passo_clicado)
            del historico_navegacao[indice + 1:]
            atualizar_painel_visual()


    def exibir_tela_final(nome_rotina):
        area_conteudo.controls.clear()
        
        # 1. Título da Rotina Atual
        titulo_rotina = ft.Text(
            f"ROTINA: {nome_rotina.upper()}", 
            size=20, 
            weight=ft.FontWeight.BOLD, 
            color=TEMA["PRIMARIA"]
        )
        
        # Se o usuário clicou especificamente em Inspeção de Linha, montamos o formulário
        if nome_rotina == "1.1. Inspeção de Linha":
            
            # 2. Criando os Campos do Formulário
            campo_lote = ft.TextField(label="Número do Lote", width=300, hint_text="Ex: LOTE-2026-01")
            
            campo_status = ft.Dropdown(
                label="Status da Inspeção",
                width=300,
                options=[
                    ft.dropdown.Option("Aprovado"),
                    ft.dropdown.Option("Reprovado"),
                    ft.dropdown.Option("Condicional")
                ]
            )
            
            # Texto invisível que usaremos para mostrar mensagens de sucesso ou erro
            texto_feedback = ft.Text("", size=14, weight=ft.FontWeight.BOLD)
            
            # 3. Lógica do Botão Salvar (O que acontece quando clica)
            def salvar_inspecao(e):
                # Capturando os valores digitados usando o .value
                lote = campo_lote.value
                status = campo_status.value
                
                # Validação simples
                if not lote or not status:
                    texto_feedback.value = "⚠️ Por favor, preencha todos os campos!"
                    texto_feedback.color = "red"
                else:
                    # Aqui você processaria os dados (gravaria num banco, geraria um TXT, etc.)
                    texto_feedback.value = f"✅ Sucesso! Lote {lote} registrado como {status}."
                    texto_feedback.color = "green"
                    
                    # Limpa os campos após salvar
                    campo_lote.value = ""
                    campo_status.value = None
                    
                page.update() # Lembra do nosso amigo de reatividade?
                
            btn_salvar = ft.ElevatedButton(
                "Gravar Inspeção", 
                icon=ft.Icons.SAVE, 
                on_click=salvar_inspecao
            )
            
            btn_voltar = ft.TextButton(
                "Voltar para Opções", 
                on_click=lambda e: atualizar_painel_visual()
            )
            
            # 4. Juntando as peças na Coluna de Conteúdo
            form_container = ft.Column([
                campo_lote,
                campo_status,
                texto_feedback,
                ft.Container(height=10),
                ft.Row([btn_salvar, btn_voltar], alignment=ft.MainAxisAlignment.CENTER)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15)
            
            area_conteudo.controls.append(ft.Column([titulo_rotina, ft.Container(height=15), form_container], horizontal_alignment=ft.CrossAxisAlignment.CENTER))
            
        else:
            # Para as outras telas, mantém o aviso antigo temporariamente
            aviso_construcao = ft.Text("Módulo de captura de dados em desenvolvimento...", italic=True)
            btn_voltar = ft.ElevatedButton("Voltar para Opções", icon=ft.Icons.ARROW_BACK, on_click=lambda e: atualizar_painel_visual())
            
            area_conteudo.controls.append(
                ft.Column([titulo_rotina, ft.Container(height=20), aviso_construcao, ft.Container(height=30), btn_voltar], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            )
            
        page.update()

    def exibir_tela_final_111(nome_rotina):
        # Quando chega em uma tela de verdade (Inspeção, Checklist, etc.)
        area_conteudo.controls.clear()
        
        titulo_rotina = ft.Text(f"ROTINA: {nome_rotina.upper()}", size=20, weight=ft.FontWeight.BOLD, color=TEMA["PRIMARIA"])
        aviso_construcao = ft.Text("Módulo de captura de dados em desenvolvimento...", italic=True)
        
        btn_voltar = ft.ElevatedButton(
            "Voltar para Opções", 
            icon=ft.Icons.ARROW_BACK,
            on_click=lambda e: atualizar_painel_visual()
        )
        
        area_conteudo.controls.append(
            ft.Column([
                titulo_rotina,
                ft.Container(height=20),
                aviso_construcao,
                ft.Container(height=30),
                btn_voltar
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )
        page.update()

    # --- COMPONENTES LOCAIS ---
    linha_caminho = ft.Row(spacing=5, wrap=True, alignment=ft.MainAxisAlignment.START)
    painel_opcoes = ft.Column(spacing=10, width=500)
    area_conteudo = ft.Column(alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # Bloco do menu interno
    corpo_sistema = ft.Container(
        content=ft.Column([
            ft.Container(content=linha_caminho, padding=ft.padding.only(top=10, bottom=5)),
            ft.Container(height=5),
            area_conteudo 
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=ft.padding.symmetric(horizontal=20),
        width=600
    )

    page.padding = 0 
    page.spacing = 0

    # Montagem final
    componentes_tela = ft.Column([
        criar_header_sistema(TEMA,"settings","Sistema de Controle de Qualidade",TEMA["TEXTO_CLARO"],TEMA["PRIMARIA"]), 
        corpo_sistema
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    page.add(componentes_tela)
    
    # Inicializa construindo o primeiro nível do menu
    atualizar_painel_visual()

ft.app(target=main)
