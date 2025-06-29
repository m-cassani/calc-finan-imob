import matplotlib.pyplot as plt

def plot_exemplo(saldo):
    fig, ax = plt.subplots(figsize=(6, 4))
    fig.subplots_adjust(bottom=0.2, left=0.15)  # aumentar margens
    ax.plot(saldo, marker='o')
    ax.set_title('Evolução do Saldo Devedor')
    ax.set_xlabel('Meses')
    ax.set_ylabel('Saldo (R$)')
    ax.grid(True)
    return fig
