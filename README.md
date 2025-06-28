# Calculadora de Financiamento Imobiliário para Tabelas SAC/PRICE

Estrutura do projeto

```
calc-finan-imob/
│
├── main.py                  # Arquivo principal que inicia a aplicação
├── requirements.txt         # Dependências do projeto
├── README.md                # Documentação básica
│
├── /app                     # Lógica da aplicação
│   ├── __init__.py
│   ├── calculator.py        # Módulo com as funções de cálculo (SAC e PRICE)
│   ├── plots.py             # Módulo responsável pelos gráficos
│   └── utils.py             # Funções auxiliares (formatar valores, etc.)
│
├── /gui                     # Interface gráfica
│   ├── __init__.py
│   ├── layout.py            # Layout e criação das telas
│   └── controller.py        # Faz a ponte entre GUI e cálculos
│
├── /assets                  # Imagens, ícones ou arquivos auxiliares (opcional)
│
└── /dist                    # Pasta onde ficarão os executáveis gerados (criada após empacotamento)
```
