import plotly.graph_objects as go
import plotly
import os
import sys

def plot_window_plotly(x, y, z, c1='blues', c2='jet', smooth=True, title='Graph'):
    from PyQt5.QtCore import QUrl
    from PyQt5.QtWebEngineWidgets import QWebEngineView
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QIcon

    fig = plotly.subplots.make_subplots(rows=2, cols=2,
                                        specs=[[{'type' : 'surface'}, {'type' : 'surface'}],
                                                [{'type' : 'heatmap'}, {'type' : 'heatmap'}]])

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

    fig.update_layout(title=title, margin=dict(l=65, r=50, b=65, t=90), height=800, width=1000)


    plotly.offline.plot(fig, filename='graph_plot.html', auto_open=False)

    app = QApplication(sys.argv) #Cria a aplicação
    web = QWebEngineView() #Cria a view
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "graph_plot.html")) #Recupera o diretório onde está localizada a página HTML criada pelo Plotly Offline
    web.load(QUrl.fromLocalFile(file_path)) #Carrega a página criada pelo Plotly Offline
    web.setWindowTitle('PLOT 3D - LNDC') #Título da aplicação
    web.setGeometry(500, 150, 1050, 800) #Define o tamanho e posicionamento da tela
    web.setFixedSize(1050, 800) #Fixa o tamanho da tela e não permite redimensionamento
    web.setWindowIcon(QIcon('lndc.jpg')) #Ícone da aplicação
    web.show() #Exibe a página dentro da aplicação
    sys.exit(app.exec_())
