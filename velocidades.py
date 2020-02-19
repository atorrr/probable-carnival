import numpy as np
import matplotlib.pyplot as plt

# Recta 1.4t (aceleración de 1.4 m/s^2)
tiempos = np.arange(1.0, 31.0)
vel_real = 0.14 * tiempos
vel_rand = vel_real + 0.5 * (2.0 * np.random.rand(len(vel_real)) - 1.0)

f = open('velocidades.dat', 'w')

for i in range(len(tiempos)):
    escribe = str(tiempos[i]) + '\t' + str(vel_rand[i]) + '\n'
    f.write(escribe)

#plt.plot(tiempos, vel_real)
plt.plot(tiempos, vel_rand, 'o')
plt.show()
