from data import plot_funcs
from data.read_funcs import *

def main():
    x, y, z = read_arq3()
    plot_funcs.plot_plotly(x, y, z)

if __name__ == '__main__':
    main()