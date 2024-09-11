import flet as ft


def main(page: ft.Page):
    page.title="¿app03?"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.bgcolor="black"
    
    lbl1=ft.Text("¿digits?",
                style=ft.TextStyle(size=40,weight="bold"))
                                    
    img1=ft.Image(src="gorra.png",width=200,height=200)
    
    btnprimer_numero=ft.ElevatedButton("primer_numero",
    color="red",
    width=100,
    height=50)
    
    btnsegundo_numero=ft.ElevatedButton("segundo_numero",
    color="red",
    width=100,
    height=50)
    
def pair_number(e):
    btnprimer_numero.width+=30
    btnsegundo_numero.height+=10
    page.update()

def si(e):
    Img1.src="gorra.png"
    page.undate()    
    
    
    btnprimer_numero.on_click=numero
    btnsegundo_numero.on_click=numero
    
    
    
    page.add(
        ft.column(
            [
                lbl1,
                img1,
                ft.Row([btnprimer_numero,btnsugundo_numero],
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.app(main)
