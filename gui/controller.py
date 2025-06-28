import PySimpleGUI as sg
from app.calculator import exemplo_calculo
from app.plots import plot_exemplo
from gui.layout import draw_plot

def run_event_loop(window):
    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, 'Sair'):
            break

        if event == 'Calcular':
            # Coletar dados
            tipo = values['-TIPO-']
            valor_imovel = float(values['-VALOR-'])
            entrada = float(values['-ENTRADA-'])
            prazo = int(values['-PRAZO-'])
            juros = float(values['-JUROS-'])
            tr = float(values['-TR-'])
            extra = float(values['-EXTRA-'])

            # Exemplo de retorno de cálculo (temporário)
            tabela, saldo = exemplo_calculo(prazo)

            # Atualizar tabela
            window['-TABELA-'].update(values=tabela)

            # Atualizar gráfico
            fig = plot_exemplo(saldo)
            draw_plot(window['-CANVAS-'], fig)

    window.close()
