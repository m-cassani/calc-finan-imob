from app.utils import formatar_moeda
from datetime import datetime

def calcular_financiamento(tipo, valor_imovel, entrada, prazo, juros_anual, tr_anual, amort_extra):
    valor_financiado = valor_imovel - entrada
    saldo_devedor = valor_financiado
    tabela = []
    saldo = []

    # Ajuste para taxa efetiva mensal a partir da taxa efetiva anual
    juros_anual_efetiva = juros_anual / 100
    juros_mensal = (1 + juros_anual_efetiva) ** (1/12) - 1

    tr_mensal = tr_anual / 100 / 12  # TR mensal calculada mas atualmente não usada

    ano = datetime.now().year
    mes = datetime.now().month

    total_pago = 0
    total_juros = 0

    if tipo == 'SAC':
        amortizacao_base = valor_financiado / prazo

        while saldo_devedor > 0:
            amortizacao = amortizacao_base + amort_extra
            juros = saldo_devedor * juros_mensal
            parcela = amortizacao + juros

            # Ajuste final para não amortizar além do saldo
            if saldo_devedor - amortizacao < 0:
                amortizacao = saldo_devedor
                parcela = amortizacao + juros
                saldo_devedor = 0
            else:
                saldo_devedor -= amortizacao

            # Somar totais depois do ajuste final
            total_pago += parcela
            total_juros += juros

            tabela.append([
                f'{mes:02d}/{ano}',
                formatar_moeda(parcela),
                formatar_moeda(amortizacao),
                formatar_moeda(juros),
                formatar_moeda(saldo_devedor)
            ])
            saldo.append(saldo_devedor)

            mes += 1
            if mes > 12:
                mes = 1
                ano += 1

            if len(tabela) > 1000:
                break

    elif tipo == 'PRICE':
        parcela_fixa = (valor_financiado * juros_mensal) / (1 - (1 + juros_mensal) ** (-prazo))

        while saldo_devedor > 0:
            juros = saldo_devedor * juros_mensal
            amortizacao = parcela_fixa - juros

            # Somar amortização extraordinária à amortização do mês
            amortizacao_total = amortizacao + amort_extra

            # Ajuste para não amortizar além do saldo
            if saldo_devedor - amortizacao_total < 0:
                amortizacao_total = saldo_devedor
                saldo_devedor = 0
            else:
                saldo_devedor -= amortizacao_total

            parcela = amortizacao + juros  # parcela fixa, não considera extra na parcela

            # Acumular totais: parcela fixa + amort_extra (que é antecipação, mas paga no mês)
            total_pago += parcela + amort_extra
            total_juros += juros

            tabela.append([
                f'{mes:02d}/{ano}',
                formatar_moeda(parcela + amort_extra),
                formatar_moeda(amortizacao_total),
                formatar_moeda(juros),
                formatar_moeda(saldo_devedor)
            ])
            saldo.append(saldo_devedor)

            mes += 1
            if mes > 12:
                mes = 1
                ano += 1

            if len(tabela) > 1000:
                break

    tempo_meses = len(tabela)

    resumo = {
        'valor_financiado': formatar_moeda(valor_financiado),
        'valor_total_pago': formatar_moeda(total_pago),
        'valor_total_juros': formatar_moeda(total_juros),
        'tempo_meses': f'{tempo_meses} meses'
    }

    return tabela, saldo, resumo
