from constantes import *
from math import pi
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


def modelo(T, t):
    Tv=T[0]
    Tr=T[1]
    Q1=  (Tamb - Tv)      /(e/(2*kvidro*2*pi*r*altura) + 1/(h*2*pi*r*altura))
    Q2 = (Tv - Tr)        /(e/(2*kvidro*2*pi*r*altura))
    Q3 = (Tamb-Tr)        /(et/(ktampa*pi*r**2) + 1/(h * pi * r **2))
    Q4 = (Tamb**4 - Tr**4)/(1/(er*sigma*pi*r**2))
    # Q1=  (Tamb - Tv)      /(e/((2*kvidro)*2*pi*(r + 0.75*e)*altura) + 1/(h*2*pi*(r+e)*altura))
    # Q2 = (Tv - Tr)        /(e/(2*kvidro*2*pi*(r+0.25*e)*altura))
    # Q3 = (Tamb-Tr)        /(et/(ktampa*pi*r**2) + 1/(h * pi * r **2))
    # Q4 = (Tamb**4 - Tr**4)/(1/(er*sigma*pi*r**2))
    dTrdt = (Q1+Q3+Q4)/(Mli*Ccoca)
    dTvdt = (Q1-Q2)/(Mvi*Cvidro)
    dxdt = [dTvdt, dTrdt]
    return dxdt


#Construção do grafico conclusivo:

espessura = np.arange(0.001, 10, 0.1)

#Calculo do tempo ate atingir 90% da Tamb

Trel = 0.9*25 + 273

def modeloc(T, t, e):
    Tv=T[0]
    Tr=T[1]
    Q1=  (Tamb - Tv)      /(e/(2*kvidro*2*pi*r*altura) + 1/(h*2*pi*r*altura))
    Q2 = (Tv - Tr)        /(e/(2*kvidro*2*pi*r*altura))
    Q3 = (Tamb-Tr)        /(et/(ktampa*pi*r**2) + 1/(h * pi * r **2))
    Q4 = (Tamb**4 - Tr**4)/(1/(er*sigma*pi*r**2))
    # Q1=  (Tamb - Tv)      /(e/((2*kvidro)*2*pi*(r + 0.75*e)*altura) + 1/(h*2*pi*(r+e)*altura))
    # Q2 = (Tv - Tr)        /(e/(2*kvidro*2*pi*(r+0.25*e)*altura))
    # Q3 = (Tamb-Tr)        /(et/(ktampa*pi*r**2) + 1/(h * pi * r **2))
    # Q4 = (Tamb**4 - Tr**4)/(1/(er*sigma*pi*r**2))
    dTrdt = (Q1+Q3+Q4)/(Mli*Ccoca)
    dTvdt = (Q1-Q2)/(Mvi*Cvidro)
    dxdt = [dTvdt, dTrdt]
    return dxdt

x=273
y=273
T_0 = [x,y]
dt = 1
tempo = np.arange(0,36000*8,dt)
tmin = [0]*len(espessura)

for i in range(len(espessura)):
    w = odeint(modeloc, T_0, tempo, args = (espessura[i],))
    Tr = w[:,1]
    for j in range(len(Tr)):
        if Tr[j]>=Trel:
            tmin[i] = tempo[j]/3600
            break   

plt.plot(espessura, tmin)
plt.title("Gráfico conclusivo")
plt.xlabel("espessura(m))")
plt.ylabel("tempo(horas)")
plt.grid()
plt.show()
