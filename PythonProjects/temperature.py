import matplotlib.pyplot as plt

localidades = ['Santa Úrsula', 'Fazenda Ponte', 'Sentamento Salgado', 'Boa Hora', 'Cachoeira dos Fragosos']
temperatura = [27.5, 27.30, 26.30, 30.40, 28.20]


plt.title("DATA SETS LEITE DO FUTURO:", fontsize = 18)
plt.bar(localidades, temperatura, color = 'red', label = 'temperatura')
plt.xlabel('Localidades')
plt.ylabel('Temperatura (ºC)')
plt.legend(fontsize=14)
plt.show()