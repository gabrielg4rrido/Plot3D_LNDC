import numpy as np
import  interp_plot_funcs

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


interp_plot_funcs.plot_window_plotly(x, y, z, title='Plot 3D', smooth=True)
#interp_plot_funcs.interp_plot(x, y, z)