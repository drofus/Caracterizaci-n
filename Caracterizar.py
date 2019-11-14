#!/usr/bin/env python
#-*-coding: utf-8-*-

import numpy as np
import matplotlib.pyplot as plt

#Datos
x = (138,131,159,161,163,147,166,141,173,168,139,192,187,122,184,185,193)

y = (160659,16789,23084,18785,15915,66262,11207,120926,5715,9680,125695,1045,1698,64601,2434,2396,865)

z = 30-(2.512*np.log10(y))


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

