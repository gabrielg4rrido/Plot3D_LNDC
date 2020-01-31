from data import plot_funcs
from data.read_funcs import *

def main():
    x, y, z = read_arq2()
    plot_funcs.plot_plotly(x, y, z, title='Permeabilidade Magnética')
    print("ACABOU")

if __name__ == '__main__':
    main()