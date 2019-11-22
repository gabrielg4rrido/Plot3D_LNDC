import numpy as np
import plotly.graph_objs as go
import plotly.offline
import os, sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5 import QtWebEngineWidgets

nomeArq = 'EstudoAntigo2_difAmpZ.txt'
cabecalho = 15

arq = open(nomeArq,'r')

dataArray = []
for i in range(cabecalho):
    if i == 8:
        rotLine = arq.readline()
        rotData = rotLine.replace('\n','').split(';')
        rotVal = [int(v) for v in rotData]
    elif i == 11:
        gvLine = arq.readline()
        gvData = gvLine.split(';')
        gvVal = [int(v) for v in gvData]
    else:
        aux = arq.readline()

for line in arq:
    dataStr = line.split(';')
    dataVals = [float(v) for v in dataStr]
    dataArray.append(dataVals)

dataArray = np.array(dataArray, dtype = 'float')

x = list(range(gvVal[0], gvVal[1]+1, gvVal[2]))
y = list(range(rotVal[0], rotVal[1]+1, rotVal[2]))
z = dataArray



class PlotlyViewer(QtWebEngineWidgets.QWebEngineView):
    def __init__(self, x, y, z, c1='blues', c2='jet', smooth=True, title='Graph', exec=True):

        # Cria uma instância de QApplication ou usa uma que já existe
        self.app = QApplication.instance() if QApplication.instance() else QApplication(sys.argv)
        super().__init__()

        #Cria os plots
        fig = plotly.subplots.make_subplots(rows=2, cols=2,
                                            specs=[[{'type': 'surface'}, {'type': 'surface'}],
                                                   [{'type': 'heatmap'}, {'type': 'heatmap'}]])

        fig.add_trace(go.Surface(x=x, y=y, z=z, colorscale=c1, showscale=False), row=1, col=1)
        fig.update_traces(contours_z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True))
        fig.add_trace(go.Surface(x=x, y=y, z=z, colorscale=c2), row=1, col=2)
        fig.update_traces(contours_z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True))

        if (smooth):
            fig.add_trace(go.Heatmap(x=x, y=y, z=z, colorscale=c1, showscale=False, zsmooth='best', connectgaps=True),
                          row=2, col=1)
            fig.add_trace(go.Heatmap(x=x, y=y, z=z, colorscale=c2, showscale=False, zsmooth='best', connectgaps=True),
                          row=2, col=2)
        else:
            fig.add_trace(go.Contour(x=x, y=y, z=z, colorscale=c1, showscale=False, line_width=0), row=2, col=1)
            fig.add_trace(go.Contour(x=x, y=y, z=z, colorscale=c2, showscale=False, line_width=0), row=2, col=2)

        fig.update_layout(title=title, margin=dict(l=65, r=50, b=65, t=90), height=800, width=1000)

        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "graph_plot.html")) #Recupera o diretório onde está localizada a página HTML criada pelo Plotly Offline
        plotly.offline.plot(fig, filename=self.file_path, auto_open=False)

        self.load(QUrl.fromLocalFile(self.file_path)) #Carrega a página criada pelo Plotly Offline
        self.setWindowTitle('PLOT 3D - LNDC')  # Título da aplicação
        self.setGeometry(500, 150, 1050, 800)  # Define o tamanho e posicionamento da tela
        self.setFixedSize(1050, 800)  # Fixa o tamanho da tela e não permite redimensionamento
        self.setWindowIcon(QIcon('lndc.jpg'))  # Ícone da aplicação
        self.show()  # Exibe a página dentro da aplicação

        if exec:
            self.app.exec_()

    def closeEvent(self, event):
        os.remove(self.file_path)


main = PlotlyViewer(x, y, z)