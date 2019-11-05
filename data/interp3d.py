import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d   #Necessário para plot 3D
import scipy.interpolate as interp
import interp3dfunc
from matplotlib.ticker import LinearLocator, FormatStrFormatter


x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

z =  np.array([[0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 1, 1, 0, 0],
               [0, 0, 1, 1, 0, 0],
               [0, 0, 2, 2, 0, 0],
               [0, 0, 2, 2, 0, 0],
               [0, 0, 1, 1, 0, 0],
               [0, 0, 1, 1, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0]])

interp3dfunc.interp_plot(x, y, z)