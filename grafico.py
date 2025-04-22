from funcoes import modelo
import pandas
from constantes import *
from math import pi
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

#Grafico inicial
x=273.15 + 0
y=273.15 + 0
T_0 = [x,y]
dt = 0.01
tempo = np.arange(0,3600 * 10,dt)

a = odeint(modelo, T_0, tempo)

Tv = a[:,0]
Tr = a[:,1]    

plt.plot(tempo/3600, Tr-273.15,'r-' , label="Temperatura do refrigerante")
plt.plot(tempo/3600, Tv-273.15,'k--', label="Temperatura do vidro")
plt.title("Temperatura Coca e Vidro x tempo")
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.xlabel("Tempo(horas)")
plt.ylabel("Temperatura(°C)")
plt.legend()
plt.grid()
plt.show()
#Gráfico do teste
colunas = ['t', 'Tliq']
dados = pandas.read_csv('planilha_convertida_ponto.csv', names=colunas)
lista_tempo_csv = dados.t.tolist()
lista_Tliq_csv = dados.Tliq.tolist()

# plt.plot(tempo/3600, Tv-273.15,'r--' , label="Temperatura do vidro")
# plt.plot(lista_tempo_csv, lista_Tliq_csv,"g-", label="Validação")
# plt.plot(tempo/3600, Tr-273.15,'r--' , label="Temperatura do refrigerante")
# plt.title("Primeira iteração")
# plt.xlabel("Tempo(horas)")
# plt.ylabel("Temperatura(°C)")
# plt.legend()
# plt.grid()
# plt.show()

# erro percentual médio
listatsegundos = []
dif = 0
for temp in lista_tempo_csv:
    listatsegundos.append(int(temp*3600))
for i in range(len(lista_Tliq_csv)):
    tempola = int(listatsegundos[i] / dt)
    dif +=  lista_Tliq_csv[i] - (Tr[tempola] - 273.15) #(realizado - previsto)
print(dif/len(listatsegundos))    

# plot resultado do experimento

for i in range(len(Tr)):
    if Tr[i] >= 17.46+273.15:
        tmax = tempo[i] / 3600
        trmax = Tr[i] - 273.15
        break

gradex = [tmax]*len(Tr)
gradey = [trmax]*len(Tr)
print(tmax)
plt.plot(tempo/3600, Tr-273.15,'r-' , label="Temperatura do refrigerante")
plt.plot(gradex, Tr-273.15, 'k--')
plt.plot(tempo/3600, gradey, 'k--')
plt.plot(tmax, trmax, "bo", markersize=8 )
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.xlabel("Tempo(horas)")
plt.ylabel("Temperatura(°C)")
plt.legend()
plt.grid()
plt.show()

