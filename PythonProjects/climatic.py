import matplotlib.pyplot as plt

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
precipitacao = [140, 232, 350, 358, 260, 139, 98, 43, 37, 34, 25, 54]
temperatura = [27.2, 26.8, 26.5, 26.7, 26.0, 26.5, 25.7, 26.1, 26.7, 27.2, 27.3, 27.5 ]

plt.title("PRECIPITAÇÃO PLUVIOMÉTRICA MÉDIA EM FORTALEZA-CE", fontsize=16)
plt.bar(meses, precipitacao, color ='blue', label='mm')
plt.plot(meses, temperatura, color='red', label="°C")
plt.xlabel('Meses')
plt.ylabel('Números')
plt.grid()
plt.legend(fontsize=14)
plt.show()
