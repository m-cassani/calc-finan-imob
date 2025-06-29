import re

def formatar_moeda(valor):
    return f'R$ {valor:,.2f}'.replace('.', ',').replace(',', '.', 1)

def desformatar_moeda(valor_formatado):
    # Remove tudo que não for número ou vírgula
    valor_limpo = re.sub(r'[^\d,]', '', valor_formatado)
    # Troca vírgula por ponto decimal
    return float(valor_limpo.replace(',', '.'))

def formatar_porcentagem(valor):
    return f'{valor:.2f}%'
