import flet as ft

BG_WHITE = '#FAFAFA'
FONT_COLOR = '#000000'
FOREST_GREEN = '#228B22'

nomes = ['Davi', 'Rafael', 'Ramon', 'Julia', 'André', 'João']

def main(page: ft.Page):
    page.title = "Participantes"
    page.bgcolor = BG_WHITE

    page.add(
        ft.Row(
            [
                ft.Text("Sorteador", size=32, color=FOREST_GREEN)
            ], 
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    lv_nomes = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    for i, nome in enumerate(nomes, start=1):
        lv_nomes.controls.append(
            ft.Text(f'{i}. {nome}', color=FONT_COLOR, size=16)
        )

    page.add(lv_nomes)

    

ft.app(main)
