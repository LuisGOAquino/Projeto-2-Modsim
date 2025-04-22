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

espessura = np.arange(0.001, 0.1,0.001)
espessura = np.arange(0.001, 100, 1)
#Calculo do tempo ate atingir 90% da Tamb

Trel =17.46+273.15

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

Tv_0 = 273.15
Tr_0 = 273.15
T_0 = [Tv_0, Tr_0]
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
espusada = [0.004532] * len(tmin)
# plot do gráfico 2 de conclusão - espessura menor range

# plt.plot(espessura*1000, tmin)
# plt.plot(4.532, 2.5015888888888886,"ro" , markersize= 8)
# plt.xlim(left=0)
# plt.ylim(bottom=0)
# plt.title("Gráfico conclusivo")
# plt.xlabel("espessura(mm)")
# plt.ylabel("tempo(horas)")
# plt.grid()
# plt.show()

# plot do gráfico 3 de conclusão - range de espessura grande

for j in range(len(espessura)):
    if tmin[j]>=38.7:
        break 

plt.plot(espessura, tmin, 'r-')
plt.plot(espessura[j], tmin[j], 'ko', markersize = 10)
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.title("Gráfico conclusivo")
plt.xlabel("espessura(m)")
plt.ylabel("tempo(horas)")
plt.grid()
plt.show()