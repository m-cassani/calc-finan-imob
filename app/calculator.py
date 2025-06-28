def exemplo_calculo(prazo):
    # Exemplo fictício de parcelas para demonstrar a interface
    tabela = []
    saldo = []
    saldo_atual = 100000  # Exemplo de saldo inicial

    for mes in range(1, prazo + 1):
        parcela = 1000 + mes  # Apenas um valor aleatório
        amortizacao = 500
        juros = parcela - amortizacao
        saldo_atual -= amortizacao

        tabela.append([f'{mes}/2025', f'{parcela:.2f}', f'{amortizacao:.2f}', f'{juros:.2f}', f'{saldo_atual:.2f}'])
        saldo.append(saldo_atual)

        if saldo_atual <= 0:
            break

    return tabela, saldo
