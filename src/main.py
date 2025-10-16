import flet as ft
import requests as rq
import json
from time import sleep

def main(pagina: ft.Page):
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    pagina.theme_mode = 'dark'

    computador = ft.Icon(name=ft.Icons.FAVORITE, color=ft.Colors.PINK)
    
    
    def config_brn_desligar(e):
        conputador_ = 'https://computadores-aa482-default-rtdb.firebaseio.com/computador/.json'
        data = {'btn': 1}
        rq.patch(url=conputador_ ,data=json.dumps(data))
        
    
    btn_desligar = ft.ElevatedButton('Desligar', width=150, on_click=config_brn_desligar)
    
    base = ft.Container(
        content=(ft.Column([ft.Row([ft.Text('computador', size=25), computador], alignment='center'), ft.Row([btn_desligar],alignment='center')]))

        
    )
    

    while True:
        sleep(1)
        conputador_ligado = 'https://computadores-aa482-default-rtdb.firebaseio.com/computador/ligado/.json'
        rr = rq.get(conputador_ligado)
        if rr.text == '1':
            computador.color = '#00FF00'
            pagina.update()
        elif rr.text == '0':
            computador.color = "#FF0000"
            pagina.update()
        pagina.add(base)
ft.app(target=main)
