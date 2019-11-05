import numpy as np
import plotly.graph_objs as go
import sys, os
import plotly.offline
import  interp3dfunc
import matplotlib


def interp_plotly(fig):
    from PyQt5.QtCore import QUrl
    from PyQt5.QtWebEngineWidgets import QWebEngineView
    from PyQt5.QtWidgets import QApplication

    plotly.offline.plot(fig, filename='graph_plot.html', auto_open=False)

    app = QApplication(sys.argv)
    web = QWebEngineView()
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "graph_plot.html"))
    web.load(QUrl.fromLocalFile(file_path))
    web.show()
    web.setWindowTitle("Graph")
    sys.exit(app.exec_())
    sys.quit()


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


surface = go.Figure(data=[go.Surface(x=x, y=y ,z=z , colorscale="Jet")])
surface.update_traces(contours_z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True))
surface.update_layout(title='Graph', margin=dict(l=65, r=50, b=90, t=90))
                  #scene_camera_eye=dict(x=1.87, y=0.88, z=-0.64),
                  #margin=dict(l=65, r=50, b=65, t=90))

#contour = go.Figure(data = [go.Contour(x=x, y=y, z=z, colorscale="Jet")])

interp_plotly(surface)
