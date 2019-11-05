import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import interp3dfunc

plt.rcParams['figure.figsize'] = (9,6)

x = np.arange(0, 8*np.pi, 0.1)
y = np.cos(x)

fig, ax1 = plt.subplots()

ax1.set_title("Interp")
ax1.set_xlabel("Eixo X")
ax1.set_ylabel("Eixo Y")
ax1.plot(x, y, 'r--', label='f(x)=x²')
#ax2.plot(y, x, 'g--', label='f(x)-¹=x²')
ax1.legend()
#ax2.legend()
plt.show()

#Salva a figura atual no diretório raíz
#plt.savefig('grafico1.png', transparent=True)