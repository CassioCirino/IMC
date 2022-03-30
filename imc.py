from os import system
from PySimpleGUI import PySimpleGUI as sg
# layout
sg.theme('Reddit')
layout = [
    [sg.Text('Peso'), sg.Input(key='peso', size=(50, 1))],
    [sg.Text('Altura'), sg.Input(key='altura', size=(50, 1))],
    [sg.Button('Calcular')]
]

# janela
janela = sg.Window('Calculadora IMC',layout)

# ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos =='Calcular':
        peso=float(valores['peso'])
        altura=float(valores['altura'])
        imc = peso / (altura * altura)
        #(print(format(round(imc,2))))
        sg.popup('Seu IMC é:', format(round(imc,2)))
