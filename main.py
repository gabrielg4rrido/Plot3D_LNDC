from matplotlib.tri import Triangulation

from data import plot_funcs
from data.read_funcs import *
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    data = read_csv()
    pm = get_relative_perm_mag()

    plot_funcs.plot_plotly_heatmap(x, y, z)
    #plot_funcs.plot_plotly_surface(x, y, z)


if __name__ == '__main__':
    main()