import matplotlib.pyplot as plt
import scipy.interpolate as interp
import numpy as np
import mpl_toolkits.mplot3d
import time
import matplotlib
from pylab import rcParams
import sys, os
import plotly.offline


"""
    Recebe como parâmetros x e y, arrays que definem os pontos coordenados usados para aproximar 
    uma função f = z(x,y) e, por fim, plota na tela o gráfico em 3D de sua superfície, seu mapa de calor e seu mapa de contorno.
"""

def interp_plot(x, y, z, graph_title='Graph', interp_type='linear'):
    rcParams['figure.figsize'] = (8, 6)  # Define o tamanho da figura do gráfico
    begin = time.time()

    # Iguala o shape dos arrays
    # XX = matriz onde todas as linhas são iguais ao array X
    # YY = matriz onde todas as colunas são iguais ao array Y
    XX, YY = np.meshgrid(x, y)  

    f = interp.interp2d(x, y, z, kind=interp_type)
    n_points = 500

    # Cria um array ordenado igualmente espaçado de tamanho = n_points no intervalo [menor valor(x), maior valor(x)]
    xnew = np.linspace(start=min(x), stop=max(x), num=n_points)

    # Cria um array ordenado igualmente espaçado de tamanho = n_points no intervalo [menor valor(y), maior valor(y)]
    ynew = np.linspace(start=min(y), stop=max(y), num=n_points)  
    
    # Obtém os pontos de z através da função interpolada e dos pontos coordenados criados por xnew e ynew
    znew = f(xnew, ynew)

    XXnew, YYnew = np.meshgrid(xnew, ynew)

    plt.figure()
    ax1 = plt.axes([0.05, 0.05, 0.9, 0.9], projection='3d')  # Cria e define os limites da superfície superfície
    ax1.plot_surface(XX, YY, z)  # Plota a superfície
    ax1.set(title=graph_title, xlabel='X Axis', ylabel='Y Axis', zlabel='Z Axis')

    plt.figure()
    plt.contourf(x, y, z, cmap='jet')  # Plota o mapa de contorno da função
    plt.colorbar()  # Adiciona uma barra de calor ao gráfico
    plt.title("{}  - Contours".format(graph_title))
    plt.show()

    end = time.time()
    print("Tempo de execução: {}".format(end - begin))


def interp_plotly(fig):
    from PyQt5.QtCore import QUrl
    from PyQt5.QtWebEngineWidgets import QWebEngineView
    from PyQt5.QtWidgets import QApplication

    plotly.offline.plot(fig, filename='graph_plot.html', auto_open=False)

    app = QApplication(sys.argv)
    web = QWebEngineView()
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "name.html"))
    web.load(QUrl.fromLocalFile(file_path))
    web.show()
    sys.exit(app.exec_())