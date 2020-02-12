import numpy as np
import pylab as plt


### Lê dados de arquivos do Lucas
def read_arq1():

    with open(r'data/dados_lucas/EstudoAntigo2_difAmpZ.txt', 'r') as in_file:
        cabecalho = 15
        data_array = []

        for i in range(cabecalho):
            if i == 8:
                rot_line = in_file.readline()
                rot_data = rot_line.replace('\n','').split(';')
                rot_val = [int(v) for v in rot_data]
            elif i == 11:
                gv_line = in_file.readline()
                gv_data = gv_line.split(';')
                gv_val = [int(v) for v in gv_data]
            else:
                aux = in_file.readline()

        for line in in_file:
            string_data = line.split(';')
            values_data = [float(v) for v in string_data]
            data_array.append(values_data)

        data_array = np.array(data_array, dtype = 'float')

        x = list(range(gv_val[0], gv_val[1]+1, gv_val[2]))
        y = list(range(rot_val[0], rot_val[1]+1, rot_val[2]))
        z = data_array

        return x, y, z


### Lê dados de arquivos do Vitor - B/H
def read_arq2():
    # Listas onde os valores de B e H serão armazenados como strings, convertidos em float e a lista se tornará um NumpyArray
    data_arrayB = []
    data_arrayH = []

    # NumpyArray onde os valores de permeabilidade magnética (B/H) serão armazenados
    data_arrayPM = np.ndarray([10201, 1])

    # Leitura e armazenamento dos valores de B
    with open(r'data/dados_vitor/perm_mag/B_Yoke_ima_lab_V5.txt',
              'r') as in_file:
        # Lê as primeiras nove linhas de comentários e ignora
        for linha in range(9):
            in_file.readline()

        for linha in in_file:
            string_data = linha.split()
            values_data = [float(v) for v in string_data]
            data_arrayB.append(values_data)

        data_arrayB = np.array(data_arrayB, dtype='float')

    # Leitura e armazenamento dos valores de H
    with open(r'data/dados_vitor/perm_mag/H_Yoke_ima_lab_V5.txt',
              'r') as in_file:
        # Lê as primeiras nove linhas de comentários e ignora
        for linha in range(9):
            in_file.readline()

        for linha in in_file:
            string_data = linha.split()
            values_data = [float(v) for v in string_data]
            data_arrayH.append(values_data)

        data_arrayH = np.array(data_arrayH, dtype='float')

    # Leitura e armazenamento dos valores de B/H
    for i in range(len(data_arrayB)):
        data_arrayPM[i][0] = data_arrayB[i][2] / data_arrayH[i][2]

    for i in range(len(data_arrayPM)):
        data_arrayPM[i][0] /= 4 * np.pi * 10E-7

    return data_arrayB * 10E2, data_arrayPM


### Lê dados de arquivos do Vitor - B
def read_arq3():
    data_arrayB = []

    with open(r'data/dados_vitor/perm_mag/B_valores.txt', 'r') as in_file:
        # Lê as primeiras nove linhas de comentários e ignora
        for linha in range(9):
            in_file.readline()

        for linha in in_file:
            string_data = linha.split()
            values_data = [float(v) for v in string_data]
            data_arrayB.append(values_data)

        data_arrayB = np.array(data_arrayB, dtype='float')
        aux = data_arrayB
        data_arrayB = data_arrayB[:, 0:2]

        x = data_arrayB[:, 0]
        y = data_arrayB[:, 1]
        z = aux[:, 2]

        return x, y, z


### Lê dados de arquivos do Vitor - H
def read_arq4():
    data_arrayH = []

    with open(r'data/dados_vitor/perm_mag/H_Yoke_ima_lab_V5.txt', 'r') as in_file:
        # Lê as primeiras nove linhas de comentários e ignora
        for linha in range(9):
            in_file.readline()

        for linha in in_file:
            string_data = linha.split()
            values_data = [float(v) for v in string_data]
            data_arrayH.append(values_data)

        data_arrayH = np.array(data_arrayH, dtype='float')
        aux = data_arrayH
        data_arrayH = data_arrayH[:, 0:2]

        x = data_arrayH[:, 0]
        y = data_arrayH[:, 1]
        z = aux[:, 2]

        return x, y, z
