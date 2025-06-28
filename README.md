# Calculadora de Financiamento Imobiliário para Tabelas SAC/PRICE

## 📂 Estrutura do projeto

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

## 📝 Descrição dos Arquivos

| Arquivo/Pasta        | Descrição                                                                  |
| -------------------- | -------------------------------------------------------------------------- |
| `main.py`            | Ponto de entrada da aplicação. Inicializa a GUI e conecta tudo.            |
| `requirements.txt`   | Lista de bibliotecas necessárias (PySimpleGUI, matplotlib, etc.).          |
| `README.md`          | Explicação básica do projeto, como rodar, como empacotar.                  |
| `/app/calculator.py` | Função para calcular SAC e PRICE, considerando amortização extraordinária. |
| `/app/plots.py`      | Função para gerar o gráfico (provavelmente usando matplotlib).             |
| `/app/utils.py`      | Funções de formatação de moeda, validação de input, etc.                   |
| `/gui/layout.py`     | Cria e organiza a interface (PySimpleGUI).                                 |
| `/gui/controller.py` | Recebe inputs, chama funções de cálculo e atualiza a interface.            |
| `/assets/`           | Pasta opcional para guardar ícones, imagens, arquivos CSV, etc.            |
| `/dist/`             | Onde o executável gerado pelo PyInstaller será armazenado.                 |
