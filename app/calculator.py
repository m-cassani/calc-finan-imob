from app.utils import formatar_moeda
from datetime import datetime

def calcular_financiamento(tipo, valor_imovel, entrada, prazo, juros_anual, tr_anual, amort_extra):
    valor_financiado = valor_imovel - entrada
    saldo_devedor = valor_financiado
    tabela = []
    saldo = []

    juros_mensal = juros_anual / 100 / 12
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

            # Aplicar amortização extra separadamente
            saldo_devedor -= (amortizacao + amort_extra)

            # Correção caso amortização final ultrapasse saldo
            if saldo_devedor < 0:
                saldo_devedor = 0

            # Acumular totais com parcela fixa
            total_pago += parcela_fixa
            total_juros += juros

            tabela.append([
                f'{mes:02d}/{ano}',
                formatar_moeda(parcela_fixa),
                formatar_moeda(amortizacao + amort_extra),
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
