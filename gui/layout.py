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
        [sg.Text('Tipo de Financiamento', size=(28, 1), justification='left'),
         sg.Combo(['SAC', 'PRICE'], key='-TIPO-', default_value='SAC', size=(10, 1))],
        
        [sg.Text('Valor do Imóvel (R$)', size=(28, 1), justification='left'),
         sg.Input(key='-VALOR-', size=(15, 1), default_text='R$ 0,00')],
        
        [sg.Text('Valor de Entrada (R$)', size=(28, 1), justification='left'),
         sg.Input(key='-ENTRADA-', size=(15, 1), default_text='R$ 0,00')],

        [sg.Text('Prazo (meses)', size=(28, 1), justification='left'),
         sg.Input(key='-PRAZO-', size=(15, 1), default_text='0')],

        [sg.Text('Taxa de Juros Efetiva Anual (%)', size=(28, 1), justification='left'),
         sg.Input(key='-JUROS-', size=(15, 1), default_text='0')],

        [sg.Text('Taxa TR Anual (%)', size=(28, 1), justification='left'),
         sg.Input(key='-TR-', size=(15, 1), default_text='0')],

        [sg.Text('Amortização Extraordinária (R$/mês)', size=(28, 1), justification='left'),
         sg.Input(key='-EXTRA-', size=(15, 1), default_text='R$ 0,00')],

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
        
        [sg.HorizontalSeparator()],

        # Adicionando o resumo abaixo da tabela
        [sg.Text('Resumo do Financiamento', font=('Any', 14, 'bold'))],
        [sg.Text('Valor Financiado: ', size=(20, 1)), sg.Text('', key='-RESUMO_VALOR-', size=(20, 1))],
        [sg.Text('Valor Total Pago: ', size=(20, 1)), sg.Text('', key='-RESUMO_TOTAL-', size=(20, 1))],
        [sg.Text('Valor Total de Juros: ', size=(20, 1)), sg.Text('', key='-RESUMO_JUROS-', size=(20, 1))],
        [sg.Text('Tempo de Pagamento: ', size=(20, 1)), sg.Text('', key='-RESUMO_TEMPO-', size=(20, 1))]
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
         sg.Column(plot_column, element_justification='center', pad=(10, 10))],
    ]

    window = sg.Window('Calculadora de Financiamento Imobiliário',
                       layout,
                       finalize=True,
                       resizable=True)
    window.Maximize()
    return window
