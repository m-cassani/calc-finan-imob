def formatar_moeda(valor):
    return f'R$ {valor:,.2f}'.replace('.', ',').replace(',', '.', 1)

def formatar_porcentagem(valor):
    return f'{valor:.2f}%'
