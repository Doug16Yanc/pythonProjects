import matplotlib.pyplot as plt


localidades = ['Santa Úrsula', 'Fazenda Ponte', 'Sentamento Salgado', 'Boa Hora', 'Cachoeira dos Fragosos']
gorduras = [3.80, 5.30, 5.20, 4.50, 4.60]
solidos = [9.40, 9.30, 8.00, 9.20, 9.10]
proteinas = [3.40, 3.40, 2.90, 3.30, 3.30]
lactose = [5.10, 5.10, 4.40, 5.00, 5.00]
sais = [0.70, 0.70, 0.60, 0.70, 0.70]
densidade = [32.5, 30.9, 26.3, 31.4, 30.7]
temperatura = [27.5, 27.30, 26.30, 30.40, 28.20]
congelamento = [-0.609, -0.609, -0.521, -0.590, -0.592]
ph = [6.00, 6.00, 6.00, 6.00, 6.10]
condutividade = [4.4, 4.4, 4.4, 4.4, 4.4]

plt.title('DATA SETS NUTRICIONAL - LEITE DO FUTURO', fontsize = 18)
plt.plot(localidades, gorduras, color = 'red', label = 'gorduras')
plt.plot(localidades, solidos, color = 'blue', label = 'SNG')
plt.plot(localidades, proteinas, color = 'yellow', label = 'proteínas')
plt.plot(localidades, lactose, color = 'green', label = 'lactose')
plt.plot(localidades, sais, color = 'brown', label = 'sais')
plt.plot(localidades, densidade, color = 'orange', label = 'densidade')
plt.plot(localidades, temperatura, color = 'red', label = 'temperatura')
plt.plot(localidades, congelamento, color = 'cyan', label = 'congelamento')
plt.plot(localidades, ph, color = 'purple', label = 'ph')
plt.plot(localidades, condutividade, color = 'pink', label = 'condutividade')
plt.xlabel('Localidades')
plt.ylabel('Números')
plt.legend(fontsize = 14)
plt.show()

