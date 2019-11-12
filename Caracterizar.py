#!/usr/bin/env python
#-*-coding: utf-8-*-

import numpy as np
import matplotlib.pyplot as plt

#Datos
x = (159,166,149,161,173,138,193,168)

y = (25257,11259,57816,11782,1939,160659,865,5881)

#x = (138,176,154,193)

#y = (160659,4609,36502,865)

z = 30-(2.512*np.log(y))

#ajuste

p = np.polyfit(z,x,1)

print(p)

#valores de x calculados del ajuste

x_ajuste = p[0]*z +p[1]

plt.plot(z,x,'o')
plt.plot(z,x_ajuste,'r-')
plt.title('calibración del telescopio de 1m de venezuela')
plt.xlabel('Magnitud Instrumental')
plt.ylabel('Magnitud Real')
plt.savefig('caracterización.png')
plt.grid()
plt.show()

resultado = np.polyfit(z, x, 1, full=True)

print(resultado)

