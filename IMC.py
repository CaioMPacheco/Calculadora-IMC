from cgitb import text
from ctypes import alignment
from multiprocessing import Value
from pickle import TRUE
from tkinter import LEFT, Label, font
from turtle import left
from typing import Text
import flet as ft
from cgitb import text


#Começo da aplicação
def main(page: ft.Page):
    page.title = "Calculadora de IMC"                           #Título da aplicação
    page.vertical_alignment = ft.MainAxisAlignment.CENTER       #Coloca os objetos todos alinhados no eixo central horizontal
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER    #Coloca os objetos todos alinhodos no eixo central vertical
    page.scroll = ft.ScrollMode.AUTO                            #Coloca a opção de scroll do mouse
    page.bgcolor = ft.colors.WHITE                              #Cor de fundo
    page.window.width = 500
    page.window.height = 600

    def fechar_banner(e):
        page.banner.open = False
        page.update()

    page.appbar = ft.AppBar(title=ft.Text("Calculadora IMC", size=30, font_family=font.BOLD),
        bgcolor= ft.colors.PURPLE_100,
        center_title=True,
        leading=ft.Icon(ft.icons.CALCULATE_OUTLINED, size=50),
        leading_width=100,

    )

    def calcular(e):
        if peso.value == "" or altura.value == "" or gênero.value == "":
            page.banner.open = True
            page.update()
        else:
            valor_peso = float(peso.value)
            valor_altura = float(altura.value)

            imc = valor_peso / (valor_altura * valor_altura)
            imc = float(f"{imc:.2f}")

            IMC.value = f"Seu IMC é {imc}"

            if gênero.value == "Feminino":
                if imc < 18.5:
                    detalhes.value = "Abaixo do peso"
                elif 18.5 <= imc < 24.9:
                    detalhes.value = "Peso ideal"
                elif 25 <= imc < 29.9:
                    detalhes.value = "Sobrepeso ou Pré obeso"
                elif 30 <= imc <34.9:
                    detalhes.value = "Obeso"
                elif imc >= 35:
                    detalhes.value = "Obesidade Morbida"
            else:
                if imc < 18.5:
                    detalhes.value = "Abaixo do peso"
                elif 18.5 <= imc < 24.9:
                    detalhes.value = "Peso ideal"
                elif 25 <= imc < 29.9:
                    detalhes.value = "Sobrepeso ou Pré obeso"
                elif 30 <= imc <34.9:
                    detalhes.value = "Obeso"
                elif imc >= 35:
                    detalhes.value = "Obesidade Morbida"

        
        peso.value = ""
        altura.value = ""
        gênero.value = ""

        page.update()
    page.banner = ft.Banner(bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text("Preencha todos os campos!"),
        actions=[
            ft.TextButton("Ok", on_click=fechar_banner),
        ],
    )


    altura= ft.TextField(label="Altura", hint_text="Por favor coloque sua altura")
    peso= ft.TextField(label="Peso", hint_text="Por favor coloque seu peso")
    gênero= ft.Dropdown(label="Gênero", hint_text="Escolha seu gênero de nascimento",
                        options=[
                            ft.dropdown.Option("Masculino"),
                            ft.dropdown.Option("Feminino")
                        ],)
    calcularIMC= ft.ElevatedButton(text="Calcular IMC", on_click=calcular)

    #Exibir resultado
    IMC = ft.Text("Seu IMC é ...", size=30)
    detalhes = ft.Text("Insira seus dados", size=20)

    info_resultados = ft.Column(
        controls=[
            IMC,
            detalhes
        ]
    )

    #Página

    layout = ft.ResponsiveRow([
        ft.Container(
            info_resultados,
            padding=5,
            col= {'sm':4, 'md':4, 'xl':4},
            alignment= ft.alignment.center,
        ),

        ft.Container(
            altura,
            padding=5,
            bgcolor= ft.colors.WHITE,
            col= {'sm':12, 'md':3, 'xl':3},
        ),

        ft.Container(
            peso,
            padding=5,
            col= {'sm':12, 'md':3, 'xl':3},
            bgcolor= ft.colors.WHITE,
        ),
        
        ft.Container(
            gênero,
            padding=5,
            col= {'sm':12, 'md':3, 'xl':3},
            bgcolor= ft.colors.WHITE,
        ),
        
        ft.Container(
            calcularIMC,
            padding=5,
            col= {'sm':12, 'md':3, 'xl':3},
            bgcolor= ft.colors.WHITE,
        )],
    )

    page.add(layout)
    page.update()
    
ft.app(target=main)