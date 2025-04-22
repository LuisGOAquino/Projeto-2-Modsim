from funcoes import modelo
import pandas
from constantes import *
from math import pi
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

#Grafico inicial
x=273.15 + 7.4
y=273.15 + 0
T_0 = [x,y]
dt = 0.01
tempo = np.arange(0,36000,dt)

a = odeint(modelo, T_0, tempo)

Tv = a[:,0]
Tr = a[:,1]    

#Gráfico do teste
colunas = ['t', 'Tliq']
dados = pandas.read_csv('planilha_convertida_ponto.csv', names=colunas)
lista_tempo_csv = dados.t.tolist()
lista_Tliq_csv = dados.Tliq.tolist()

# plt.plot(tempo/3600, Tv-273.15,'r--' , label="Temperatura do vidro")
plt.plot(lista_tempo_csv, lista_Tliq_csv,"g-", label="Validação")
plt.plot(tempo/3600, Tr-273.15,'r--' , label="Temperatura do refrigerante")
plt.title("Primeira iteração")
plt.xlabel("Tempo(horas)")
plt.ylabel("Temperatura(°C)")
plt.legend()
plt.grid()
plt.show()

# erro percentual médio
listatsegundos = []
dif = 0
for tempo in lista_tempo_csv:
    listatsegundos.append(int(tempo*3600))
for i in range(len(lista_Tliq_csv)):
    tempola = int(listatsegundos[i] / dt)
    dif += (Tr[tempola] - 273.15) - lista_Tliq_csv[i]
print(dif/len(listatsegundos))    