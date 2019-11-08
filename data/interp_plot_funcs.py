from pylab import rcParams
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.subplots
import scipy.interpolate as interp
import numpy as np
import mpl_toolkits.mplot3d
import time
import sys, os
import plotly.offline
import matplotlib


"""
    Recebe como parâmetros x e y, arrays que definem os pontos coordenados usados para aproximar 
    uma função f = z(x,y) e, por fim, plota na tela o gráfico em 3D de sua superfície, seu mapa de calor e seu mapa de contorno.
"""

def interp_plot(x, y, z, graph_title='Graph', interp_type='linear'):
    rcParams['figure.figsize'] = (8, 6)  # Define o tamanho da figura do gráfico
    begin = time.time()
    matplotlib.use('qt5agg')

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
    ax2 = plt.axes([0.05, 0.05, 0.9, 0.9], projection='3d')  # Define a superfície
    surface = ax2.plot_surface(XXnew, YYnew, znew, rstride=1,
                               cstride=1, cmap='jet', linewidth=0.25)  # Plota a superfície adicionando a ela seu mapa de calor
    ax2.set(title=graph_title, xlabel='X Axis', ylabel='Y Axis', zlabel='Z Axis')
    plt.colorbar(surface, shrink=0.5, aspect=5)

    plt.figure()
    plt.contourf(x, y, z, cmap='jet')  # Plota o mapa de contorno da função
    plt.colorbar()  # Adiciona uma barra de calor ao gráfico
    plt.title("{}  - Contours".format(graph_title))
    plt.show()

    end = time.time()
    print("Tempo de execução: {}".format(end - begin))



def plot_window_plotly(x, y, z, c1='blues', c2='jet', smooth=True, title='Graph'):
    from PyQt5.QtCore import QUrl
    from PyQt5.QtWebEngineWidgets import QWebEngineView
    from PyQt5.QtWidgets import QApplication

    fig = plotly.subplots.make_subplots(rows=2, cols=2,
                                        specs=[[{'type' : 'surface'}, {'type' : 'surface'}],
                                                [{'type' : 'contour'}, {'type' : 'heatmap' }]])

    fig.add_trace(go.Surface(x=x, y=y, z=z, colorscale=c1, showscale=False), row=1, col=1)
    fig.update_traces(contours_z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True))
    fig.add_trace(go.Surface(x=x, y=y, z=z, colorscale=c2), row=1, col=2)
    fig.update_traces(contours_z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True))

    if(smooth):
        fig.add_trace(go.Heatmap(x=x, y=y, z=z, colorscale=c1, showscale=False, zsmooth='best', connectgaps=True), row=2, col=1)
        fig.add_trace(go.Heatmap(x=x, y=y, z=z, colorscale=c2, showscale=False, zsmooth='best', connectgaps=True), row=2, col=2)
    else:
        fig.add_trace(go.Contour(x=x, y=y, z=z, colorscale=c1, showscale=False, line_width=0), row=2, col=1)
        fig.add_trace(go.Contour(x=x, y=y, z=z, colorscale=c2, showscale=False, line_width=0), row=2, col=2)

    fig.update_layout(title=title,  margin=dict(l=65, r=50, b=65, t=90), height=800, width=1000)


    plotly.offline.plot(fig, filename='graph_plot.html', auto_open=False)

    app = QApplication(sys.argv)
    web = QWebEngineView()
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "graph_plot.html"))
    web.load(QUrl.fromLocalFile(file_path))
    web.resize(1050, 850)
    web.show()
    sys.exit(app.exec_())