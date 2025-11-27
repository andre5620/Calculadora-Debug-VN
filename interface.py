import flet as ft

def decodificar_status_alarme(valor_hex):
   
    # Define nomes dos alarmes para cada posição de bit
    nomes_alarmes = [
        "statusCtrlSecao",           # bit 0
        "secByte1",                   # bit 1
        "existeMasterIsobus",         # bit 2
        "masterIsobus",               # bit 3
        "existeSensoresAgrosystem",  # bit 4
        "statusAgrosystemRow",        # bit 5
        "existePopulacao",            # bit 6
        "populacaoTravando"           # bit 7
    ]
    
    # Limpa entrada hex e converte para inteiro
    hex_limpo = valor_hex.replace('0x', '').replace('0X', '').strip()
    
    try:
        # Converte hex para inteiro
        valor = int(hex_limpo, 16)
        
        # Pega apenas os 8 bits inferiores (uint8_t)
        valor = valor & 0xFF
        
        # Verifica cada bit
        alarmes_ativos = []
        for pos_bit in range(8):
            # Verifica se o bit está setado (1) ou limpo (0)
            estado_bit = (valor >> pos_bit) & 1
            
            # Formata saída com indicação visual
            if estado_bit:
                alarmes_ativos.append(nomes_alarmes[pos_bit])

        return alarmes_ativos
        
    except ValueError:
        return None

def main(Page:ft.Page):
    Page.title = "Cauculadora Hexadecimal"
    Page.vertical_alignment = ft.MainAxisAlignment.CENTER
    Page.theme_mode = "LIGHT"



    def converteHexa(e):
        alarmesAtivos = decodificar_status_alarme(textoEntradaHex.value)
        if alarmesAtivos is None:
            textoResultado.value = f"Erro: valor hexadecimal inválido '{textoEntradaHex.value}'"
        elif alarmesAtivos:
            textoResultado.value = "\n ".join(alarmesAtivos)
        else:
            textoResultado.value = "Nenhum alarme ativo"
        Page.update()

    def trocarTema(e):
        if Page.theme_mode == "LIGHT":
            Page.theme_mode = "DARK"
            selecaoTema.thumb_icon = ft.Icons.DARK_MODE
        else:
            Page.theme_mode = "LIGHT"
            selecaoTema.thumb_icon =ft.Icons.LIGHT_MODE
        Page.update()

    textoEntradaHex = ft.TextField(hint_text="digite o valor hexadecimal", width=300, border_color=ft.Colors.PRIMARY)
    botaoExecutar = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_RIGHT,icon_size=45,on_click=converteHexa)
    textoResultado = ft.Text("", expand=True, text_align= ft.TextAlign.CENTER, color=ft.Colors.INVERSE_PRIMARY)



    if Page.theme_mode == "LIGHT":
        iconeSwitchTema = ft.Icons.LIGHT_MODE
    else:
        iconeSwitchTema = ft.Icons.DARK_MODE

    selecaoTema = ft.Switch(thumb_icon=iconeSwitchTema,on_change=trocarTema)

    layout = ft.Container(
        alignment=ft.alignment.center,
        content=ft.Column(

                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Calculadora Hexadecimal", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.PRIMARY),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            textoEntradaHex,
                            botaoExecutar,                    
                        ]
                    ),
                    ft.Text("Alarmes Ativos:", color=ft.Colors.PRIMARY),
                    ft.Card(
                        content=textoResultado,
                        color=ft.Colors.SURFACE_TINT,
                        width=360,
                        height=100,
                        margin=ft.margin.only(top=10,bottom=20),
                        
                    ),
                ]
            ),
            border=ft.border.all(2, ft.Colors.SECONDARY),
            border_radius=ft.border_radius.all(10),
            bgcolor= ft.Colors.SURFACE_CONTAINER_HIGHEST
    )

    Page.add(
        selecaoTema,
        layout,
    )