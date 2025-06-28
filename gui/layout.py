import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Armazenar referência para o canvas antigo
canvas_refs = {}

# Função para embutir o gráfico na interface
def draw_plot(canvas_elem, figure):
    key = canvas_elem.Key

    # Se já existir um canvas antigo, limpa
    if key in canvas_refs:
        canvas_refs[key].get_tk_widget().forget()
        canvas_refs[key].figure.clf()

    canvas = FigureCanvasTkAgg(figure, canvas_elem.Widget)
    canvas.draw()
    canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

    # Salvar referência
    canvas_refs[key] = canvas

    return canvas

def create_main_window():
    sg.theme('LightGrey1')

    # Coluna de entrada de dados
    input_column = [
        [sg.Text('Tipo de Financiamento')],
        [sg.Combo(['SAC', 'PRICE'], key='-TIPO-', default_value='SAC')],
        [sg.Text('Valor do Imóvel (R$)'), sg.Input(key='-VALOR-')],
        [sg.Text('Valor de Entrada (R$)'), sg.Input(key='-ENTRADA-')],
        [sg.Text('Prazo (meses)'), sg.Input(key='-PRAZO-')],
        [sg.Text('Taxa de Juros Anual (%)'), sg.Input(key='-JUROS-')],
        [sg.Text('Taxa TR Anual (%)'), sg.Input(key='-TR-')],
        [sg.Text('Amortização Extraordinária (R$/mês)'), sg.Input(key='-EXTRA-')],
        [sg.Button('Calcular', size=(15, 1)), sg.Button('Sair', size=(15, 1))],
    ]


    # Coluna da lista de parcelas
    parcela_column = [
        [sg.Text('Parcelas')],
        [sg.Table(values=[],
                  headings=['Mês/Ano', 'Parcela (R$)', 'Amortização', 'Juros', 'Saldo Devedor'],
                  auto_size_columns=False,
                  col_widths=[10, 15, 15, 10, 15],
                  key='-TABELA-',
                  num_rows=20,
                  justification='center',
                  enable_events=True)],
    ]

    # Coluna do gráfico
    plot_column = [
        [sg.Text('Gráfico')],
        [sg.Canvas(key='-CANVAS-')],
    ]

    layout = [
        [sg.Column(input_column, element_justification='left', pad=(10, 10)),
         sg.VSeperator(),
         sg.Column(parcela_column, element_justification='center', pad=(10, 10)),
         sg.VSeperator(),
         sg.Column(plot_column, element_justification='center', pad=(10, 10))]
    ]

    return sg.Window('Calculadora de Financiamento Imobiliário', layout, finalize=True)
