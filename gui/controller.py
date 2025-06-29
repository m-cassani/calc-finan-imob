import PySimpleGUI as sg
from app.calculator import calcular_financiamento
from app.plots import plot_exemplo
from gui.layout import draw_plot
from app.utils import formatar_moeda, desformatar_moeda

campos_moeda = ['-VALOR-', '-ENTRADA-', '-EXTRA-']

def safe_desformatar(valor_str):
    try:
        return desformatar_moeda(valor_str)
    except:
        return 0.0

def safe_float(valor_str):
    try:
        return float(valor_str.replace(',', '.'))
    except:
        return 0.0

def run_event_loop(window):
    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, 'Sair'):
            break

        # Formatação ao sair do campo moeda (opcional)
        if event in campos_moeda and values[event]:
            valor_raw = values[event]
            valor_num = safe_desformatar(valor_raw)
            window[event].update(formatar_moeda(valor_num))

        if event == 'Calcular':
            try:
                tipo = values.get('-TIPO-', 'SAC')
                valor_imovel = safe_desformatar(values.get('-VALOR-', '0'))
                entrada = safe_desformatar(values.get('-ENTRADA-', '0'))
                prazo = int(values.get('-PRAZO-', '0') or 0)
                juros = safe_float(values.get('-JUROS-', '0'))
                tr = safe_float(values.get('-TR-', '0'))
                extra = safe_desformatar(values.get('-EXTRA-', '0'))

                # Atualizar campos moeda com formato correto
                window['-VALOR-'].update(formatar_moeda(valor_imovel))
                window['-ENTRADA-'].update(formatar_moeda(entrada))
                window['-EXTRA-'].update(formatar_moeda(extra))

                tabela, saldo, resumo = calcular_financiamento(tipo, valor_imovel, entrada, prazo, juros, tr, extra)

                window['-TABELA-'].update(values=tabela)

                window['-RESUMO_VALOR-'].update(resumo['valor_financiado'])
                window['-RESUMO_TOTAL-'].update(resumo['valor_total_pago'])
                window['-RESUMO_JUROS-'].update(resumo['valor_total_juros'])
                window['-RESUMO_TEMPO-'].update(resumo['tempo_meses'])

                fig = plot_exemplo(saldo)
                draw_plot(window['-CANVAS-'], fig)

            except Exception as e:
                sg.popup_error('Erro ao processar os dados. Verifique os campos preenchidos.', str(e))

    window.close()
