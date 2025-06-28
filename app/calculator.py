def calcular_financiamento(tipo, valor_imovel, entrada, prazo, juros_anual, tr_anual, amort_extra):
    valor_financiado = valor_imovel - entrada
    saldo_devedor = valor_financiado
    tabela = []
    saldo = []

    juros_mensal = juros_anual / 100 / 12
    tr_mensal = tr_anual / 100 / 12

    if tipo == 'SAC':
        amortizacao_base = valor_financiado / prazo
        mes = 1

        while saldo_devedor > 0:
            amortizacao = amortizacao_base + amort_extra
            juros = saldo_devedor * juros_mensal
            parcela = amortizacao + juros

            if saldo_devedor - amortizacao < 0:
                amortizacao = saldo_devedor
                parcela = amortizacao + juros
                saldo_devedor = 0
            else:
                saldo_devedor -= amortizacao

            tabela.append([f'{mes}/2025', f'{parcela:.2f}', f'{amortizacao:.2f}', f'{juros:.2f}', f'{saldo_devedor:.2f}'])
            saldo.append(saldo_devedor)

            mes += 1
            if mes > 1000:  # trava de segurança para evitar loops infinitos
                break

    elif tipo == 'PRICE':
        parcela_fixa = (valor_financiado * juros_mensal) / (1 - (1 + juros_mensal) ** (-prazo))
        mes = 1

        while saldo_devedor > 0:
            juros = saldo_devedor * juros_mensal
            amortizacao = parcela_fixa - juros + amort_extra
            parcela = amortizacao + juros

            if saldo_devedor - amortizacao < 0:
                amortizacao = saldo_devedor
                parcela = amortizacao + juros
                saldo_devedor = 0
            else:
                saldo_devedor -= amortizacao

            tabela.append([f'{mes}/2025', f'{parcela:.2f}', f'{amortizacao:.2f}', f'{juros:.2f}', f'{saldo_devedor:.2f}'])
            saldo.append(saldo_devedor)

            mes += 1
            if mes > 1000:  # trava de segurança
                break

    return tabela, saldo
