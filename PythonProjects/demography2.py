import matplotlib.pyplot as plt

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto"]
nascimentos = [233412, 201104, 246053, 210215, 243573, 218472, 209488, 202982]
mortes = [116021, 100102, 118936, 110896, 128020, 124840, 123969, 116607]

plt.title("NÚMERO DE NASCIMENTOS POR MÊS NO BRASIL-2023", fontsize=16)
plt.plot(meses, nascimentos, color ='blue', label='nascimentos')
plt.bar(meses, mortes, color = 'red',label='óbitos')
plt.xlabel('Meses')
plt.ylabel('Nascimentos')
plt.legend(fontsize=14)
plt.show()