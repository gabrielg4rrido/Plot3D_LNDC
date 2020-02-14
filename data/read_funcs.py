import numpy as np
from scipy.constants import mu_0 #Constante magnética


### Lê dados de arquivos do Lucas
def read_dif_amp():

    with open(r'data/dados_lucas/EstudoAntigo2_difAmpZ.txt', 'r') as in_file:
        cabecalho = 15
        data_array = []

        # Ignora as linhas de cabeçalho
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

        # Lê os valores do arquivo e converte de string pra float
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
def read_b_h():

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

        # Lê os valores do arquivo e converte de string pra float
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

        # Lê os valores do arquivo e converte de string pra float
        for linha in in_file:
            string_data = linha.split()
            values_data = [float(v) for v in string_data]
            data_arrayH.append(values_data)

        data_arrayH = np.array(data_arrayH, dtype='float')

    # Leitura e armazenamento dos valores de B/H
    for i in range(len(data_arrayB)):
        data_arrayPM[i][0] = data_arrayB[i][2] / data_arrayH[i][2]

    for i in range(len(data_arrayPM)):
        data_arrayPM[i][0] /= mu_0

    return data_arrayB * 10E2, data_arrayPM


### Lê dados de arquivos do Vitor - B ou H
def read_unique(choose_file='b'):
    data_array = []
    choose_file = choose_file.lower()

    # Se o argumento for = B, lê o arquivo de B
    # Se o argumento for = H, lê o arquivo de H
    if choose_file == 'b':
        with open(r'data/dados_vitor/perm_mag/B_valores.txt', 'r') as in_file:
            # Lê as primeiras nove linhas de comentários e ignora
            for linha in range(9):
                in_file.readline()

            # Lê os valores do arquivo e converte de string pra float
            for linha in in_file:
                string_data = linha.split()
                values_data = [float(v) for v in string_data]
                data_array.append(values_data)

            data_array = np.array(data_array, dtype='float')
            aux = data_array
            data_array = data_array[:, 0:2]

            x = data_array[:, 0];
            y = data_array[:, 1];
            z = aux[:, 2]

            return x, y, z

    elif choose_file == 'h':
        with open(r'data/dados_vitor/perm_mag/H_Yoke_ima_lab_V5.txt', 'r') as in_file:
            # Lê as primeiras nove linhas de comentários e ignora
            for linha in range(9):
                in_file.readline()

            # Lê os valores do arquivo e converte de string pra float
            for linha in in_file:
                string_data = linha.split()
                values_data = [float(v) for v in string_data]
                data_array.append(values_data)

            data_array = np.array(data_array, dtype='float')
            aux = data_array
            data_array = data_array[:, 0:2]

            x = data_array[:, 0]; y = data_array[:, 1]; z = aux[:, 2]

            return x, y, z
    else:
        pass


def read_csv():
    import csv
    data_array = []

    with open ('data/dados_vitor/perm_mag/Plano_Campo_B.csv') as csvfile:

        #Armazena os valores do  arquivo CSV num array de strings
        string_data = [linha for linha in csv.reader(csvfile)]

        # Lê os valores do arquivo e converte de string pra float
        for linha in string_data:
            values_data = [float(x) for x in linha]
            data_array.append(values_data)

        data_array = np.array(data_array, dtype='float')

        return data_array


def get_h_values():
    """
        Cria uma função que calcula o valor de H através do polinômio do terceiro grau usando valores de B como X.
            :return: Array com valores de H.
        """

    # Recebe os valores de B através da função read_csv() e cria um array onde serão armazenados os valores de H
    data_arrayB = read_csv()
    data_arrayB = data_arrayB[:, 3]
    data_arrayH = np.ndarray([len(data_arrayB)])

    for i in range (len(data_arrayB)):
        B = data_arrayB[i]
        data_arrayH[i] = (41132 * B**3) - (111820 * B**2) + (251419 * B) - 5206.5 # Função que calcula H

    data_arrayH = np.array(data_arrayH, dtype='float')

    return data_arrayH

def get_relative_perm_mag():
    #Recebe os valores de B e H através das funções read_csv() e get_h_values() respectivamente
    data_arrayB = read_csv() ; data_arrayB = data_arrayB[:, 3]
    data_arrayH = get_h_values()
    data_arrayPM = np.ndarray([len(data_arrayB)])

    # Calcula o valor de PM = B/H
    for i in range(len(data_arrayB)):
        data_arrayPM[i] = data_arrayB[i] / data_arrayH[i]

    # Calcula a PM relativa dividindo os valores de PM pela constante magnética u0,
    for i in range(len(data_arrayPM)):
        data_arrayPM[i] /= mu_0

    print(data_arrayPM)

