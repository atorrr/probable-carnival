import numpy as np
import matplotlib.pyplot as plt

T0 = 90 # Temperatura inicial
Ta = 10 # Temperatura ambiente
k = 0.00277
t = np.arange(0.0, 2000.0, 60.0)

T_real = Ta + (T0 - Ta) * np.exp(-k * t)
T_rand = T_real + 5.0 * (2.0 * np.random.rand(len(T_real)) - 1.0)

f = open('enfr_newton.dat', 'w')

for i in range(len(t)):
    escribe = str(t[i]) + '\t' + str(T_rand[i]) + '\n'
    f.write(escribe)

#plt.plot(t, T_real)
#plt.plot(t, T_rand, 'o')
#plt.show()
