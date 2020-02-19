from pylab import rcParams
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from scipy import interpolate
import numpy as np
import time
import matplotlib
import mpl_toolkits.mplot3d
import sys, os
import plotly.offline
import plotly.subplots



def plot_matplot(x, y, z, graph_title='Graph', interp_type='quintic'):
    """
        Recebe como parâmetros x e y, arrays que definem os pontos coordenados usados para aproximar
        uma função f = z(x,y) e, por fim, plota na tela o gráfico em 3D de sua superfície, seu mapa de calor e seu mapa de contorno.
    """

    rcParams['figure.figsize'] = (8, 6)  # Define o tamanho da figura do gráfico
    rcParams['figure.dpi'] = 200

    begin = time.time()
    matplotlib.use('qt5agg')

    # Iguala o shape dos arrays
    # XX = matriz onde todas as linhas são iguais ao array X
    # YY = matriz onde todas as colunas são iguais ao array Y
    XX, YY = np.meshgrid(x, y)  

    f = interpolate.interp2d(x, y, z, kind=interp_type)
    n_points = 20

    # Cria um array ordenado igualmente espaçado de tamanho = n_points no intervalo [menor valor(x), maior valor(x)]
    x_new = np.linspace(start=min(x), stop=80, num=n_points)

    # Cria um array ordenado igualmente espaçado de tamanho = n_points no intervalo [menor valor(y), maior valor(y)]
    y_new = np.linspace(start=min(y), stop=max(y), num=n_points)
    
    # Obtém os pontos de z através da função interpolada e dos pontos coordenados criados por x_new e y_new
    z_new = f(x_new, y_new)

    XX_new, YY_new = np.meshgrid(x_new, y_new)

    # Cria superfície lisa
    plt.figure()
    ax1 = plt.axes([0.05, 0.05, 0.9, 0.9], projection='3d')  # Cria e define os limites da superfície superfície
    ax1.plot_surface(XX, YY, z)  # Plota a superfície
    ax1.set(title=graph_title, xlabel='X Axis', ylabel='Y Axis', zlabel='Z Axis')

    # Cria superfície com mapa de calor
    plt.figure()
    ax2 = plt.axes([0.05, 0.05, 0.9, 0.9], projection='3d')  # Define a superfície
    surface = ax2.plot_surface(XX_new, YY_new, z_new, rstride=1,
                               cstride=1, cmap='jet', linewidth=0.25)  # Plota a superfície adicionando a ela seu mapa de calor
    ax2.set(title=graph_title, xlabel='X Axis', ylabel='Y Axis', zlabel='Z Axis')
    plt.colorbar(surface, shrink=0.5, aspect=5)

    # Cria o mapa de contorno
    plt.figure()
    plt.contourf(XX_new, YY_new, z_new, cmap='jet')  # Plota o mapa de contorno da função
    plt.colorbar()  # Adiciona uma barra de calor ao gráfico
    plt.title("{}  - Contours".format(graph_title))

    plt.show()

    end = time.time()
    print("Tempo de execução: {}".format(end - begin))


def plot_plotly_heatmap(x, y, z, c='jet', smooth=True, title='Graph'):
    """
        Recebe como parâmetros x, y e z (arrays), c1 e c (escalas de cores), além de um booleano que define a suavidade do mapa de calor e uma string que define o título do gráfico.
        Por fim, plota na tela o gráfico em 3D de sua superfície e seu mapa de calor.
    """

    begin = time.time()

    f = interpolate.interp2d(x, y, z, kind='quintic')
    n_points = 12

    # Cria um array ordenado igualmente espaçado de tamanho = n_points no intervalo [menor valor(x), maior valor(x)]
    x_new = np.linspace(start=min(x), stop=max(x), num=n_points)

    # Cria um array ordenado igualmente espaçado de tamanho = n_points no intervalo [menor valor(y), maior valor(y)]
    y_new = np.linspace(start=min(y), stop=max(y), num=n_points)

    # Obtém os pontos de z através da função interpolada e dos pontos coordenados criados por x_new e y_new
    z_new = f(x_new, y_new)


    fig = go.Figure(data=go.Heatmap(x=x_new, y=y_new, z=z_new, colorscale=c, showscale=False, zsmooth='best', connectgaps=True))
    fig.update_layout(title=title, margin=dict(l=65, r=50, b=65, t=90), height=300, width=1250)
    fig.show()

    end = time.time()
    print("Tempo de execução: {}".format(end - begin))


def plot_plotly_surface(x, y, z, c='jet', smooth=True, title='Graph'):
    """
        Recebe como parâmetros x, y e z (arrays), c1 e c (escalas de cores), além de um booleano que define a suavidade do mapa de calor e uma string que define o título do gráfico.
        Por fim, plota na tela o gráfico em 3D de sua superfície e seu mapa de calor.
    """

    begin = time.time()

    f = interpolate.interp2d(x, y, z, kind='quintic')
    n_points = 12

    # Cria um array ordenado igualmente espaçado de tamanho = n_points no intervalo [menor valor(x), maior valor(x)]
    x_new = np.linspace(start=min(x), stop=max(x), num=n_points)

    # Cria um array ordenado igualmente espaçado de tamanho = n_points no intervalo [menor valor(y), maior valor(y)]
    y_new = np.linspace(start=min(y), stop=max(y), num=n_points)

    # Obtém os pontos de z através da função interpolada e dos pontos coordenados criados por x_new e y_new
    z_new = f(x_new, y_new)

    XX_new, YY_new = np.meshgrid(x_new, y_new)

    fig = go.Figure(data=go.Surface(x=XX_new, y=YY_new, z=z_new, colorscale=c))
    fig.update_layout(title=title, margin=dict(l=65, r=50, b=65, t=90), height=800, width=1250)
    fig.show()

    end = time.time()
    print("Tempo de execução: {}".format(end - begin))