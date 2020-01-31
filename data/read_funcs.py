import numpy as np

### Lê dados de arquivos do Lucas
def read_arq1():

    with open(r'C:\Users\gabri\PycharmProjects\PLOT3D_LNDC\data\dados_lucas\EstudoAntigo2_difAmpZ.txt', 'r') as in_file:
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
    data_arrayB = []
    data_arrayH = []
    data_arrayT = np.ndarray([10201, 1])

    with open(r'C:\Users\gabri\PycharmProjects\PLOT3D_LNDC\data\dados_vitor\perm_mag\B_Yoke_ima_lab_V5.txt', 'r') as in_file:
        for linha in in_file:
            string_data = linha.split()
            values_data = [float(v) for v in string_data]
            data_arrayB.append(values_data)

        data_arrayB = np.array(data_arrayB, dtype='float')

    with open(r'C:\Users\gabri\PycharmProjects\PLOT3D_LNDC\data\dados_vitor\perm_mag\H_Yoke_ima_lab_V5.txt', 'r') as in_file:
        for linha in in_file:
            string_data = linha.split()
            values_data = [float(v) for v in string_data]
            data_arrayH.append(values_data)

        data_arrayH = np.array(data_arrayH, dtype='float')

    for i in range(len(data_arrayB)):
        data_arrayT[i][0] = data_arrayB[i][2]/data_arrayH[i][2]

    for i in range(len(data_arrayT)):
        data_arrayT[i][0] /= 4 * np.pi * 10E-7

    np.savetxt(r'data\dados_vitor\perm_mag\Resultados.txt', X = data_arrayT, newline='\n')

    x = data_arrayB[:, 0] * 10E2
    y = data_arrayB[:, 1] * 10E2
    z = data_arrayT
    print(x.shape, y.shape, z.shape)

    return x, y, z

### Lê dados de arquivos do Vitor - B
def read_arq3():
    data_arrayB = []

    with open(r'C:\Users\gabri\PycharmProjects\PLOT3D_LNDC\data\dados_vitor\perm_mag\B_Yoke_ima_lab_V5.txt', 'r') as in_file:
        for linha in in_file:
            string_data = linha.split()
            values_data = [float(v) for v in string_data]
            data_arrayB.append(values_data)

        data_arrayB = np.array(data_arrayB, dtype='float')
        aux = data_arrayB
        data_arrayB = data_arrayB[:, 0:2] * 10E2

        x = data_arrayB[:, 0]
        y = data_arrayB[:, 1]
        z = aux[:, 2]

        return x, y, z

def read_arq4():
    data_arrayH = []

    with open(r'C:\Users\gabri\PycharmProjects\PLOT3D_LNDC\data\dados_vitor\perm_mag\H_Yoke_ima_lab_V5.txt', 'r') as in_file:
        for linha in in_file:
            string_data = linha.split()
            values_data = [float(v) for v in string_data]
            data_arrayH.append(values_data)

        data_arrayH = np.array(data_arrayH, dtype='float')
        aux = data_arrayH
        data_arrayH = data_arrayH[:, 0:2] * 10E2

        x = data_arrayH[:, 0]
        y = data_arrayH[:, 1]
        z = aux[:, 2]

        return x, y, z

