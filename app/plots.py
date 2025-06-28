import matplotlib.pyplot as plt

def plot_exemplo(saldo):
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot(saldo, marker='o')
    ax.set_title('Evolução do Saldo Devedor')
    ax.set_xlabel('Meses')
    ax.set_ylabel('Saldo (R$)')
    ax.grid(True)
    return fig
