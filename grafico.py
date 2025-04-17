from funcoes import*

#Grafico inicial
x=273.15 + 7.4
y=273.15 + 0
T_0 = [x,y]
dt = 0.01
tempo = np.arange(0,36000,dt)

a = odeint(modelo, T_0, tempo)

Tv = a[:,0]
Tr = a[:,1]    

plt.plot(tempo/3600, Tv-273.15, label="Temperatura do vidro")
plt.plot(tempo/3600, Tr-273.15,'r--' , label="Temperatura do refrigerante")
plt.title("Primeira iteração")
plt.xlabel("Tempo(horas)")
plt.ylabel("Temperatura(°C)")
plt.legend()
plt.grid()
plt.show()