from constantes import *
from math import pi
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def Q1(T):
    Tv=T[0]
    Tr=T[1]
    RcondVf = e / ((2*kvidro)*2*pi*(r + 0.75*e)*altura)
    RconvV = 1 / (h*2*pi*(r+e)*altura)
    F1 = (Tamb - Tv)/(RcondVf + RconvV)
    return F1

def Q2(T):
    Tv=T[0]
    Tr=T[1]
    Rcondvb = e / (2*kvidro*2*pi*(r+0.25*e)*altura)
    F2 = abs(Tv - Tr) / Rcondvb
    return F2

def Q3(T):
    Tv=T[0]
    Tr=T[1]
    Rcondt = et /(ktampa*pi*r**2)
    Rconvt = 1/(h * pi * r **2)
    F3 = (Tamb-Tr)/(Rcondt+Rconvt)
    return abs(F3)

def Q4(T):
    Tv=T[0]
    Tr=T[1]
    Rrad = 1/(er*sigma*pi*r**2)
    F4 = (Tamb**4 - Tr**4)/Rrad
    return abs(F4)

def modelo(T, t):
    Qum = Q1(T)
    Qdois = Q2(T)
    Qtres = Q3(T)
    Qquatro = Q4(T)
    dTrdt = (Qdois+Qtres+Qquatro)/(Mli*Ccoca)
    dTvdt = (Qum-Qdois)/(Mvi*Cvidro)
    dxdt = [dTrdt, dTvdt]
    return dxdt

x=273
y=273
T_0 = [x,y]
dt = 0.01
tempo = np.arange(0,36000,dt)


a = odeint(modelo, T_0, tempo)

Tv = a[:,0]
Tr = a[:,1]

for i in range(len(Tv)):
    if Tv[i]>=297.5:
        itemp = i*dt
        break
print(itemp)        

plt.plot(tempo, Tv, label="Temperatura do vidro")
plt.plot(tempo, Tr,'r--' , label="Temperatura do refrigerante")
plt.title("Primeira iteração")
plt.xlabel("Tempo(s)")
plt.ylabel("Temperatura(K)")
plt.legend()
plt.grid()
plt.show()