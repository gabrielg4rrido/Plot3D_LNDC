from data import plot_funcs
from data.read_funcs import *

def main():
    #a, b, c = read_arq3()
    #plot_funcs.plot_plotly(a, b, c, title='Densidade de fluxo magnético')

    read_arq2()
    #plot_funcs.plot_plotly(a[:, 0], a[:, 1], b, title='Permeabilidade Magnética')

if __name__ == '__main__':
    main()