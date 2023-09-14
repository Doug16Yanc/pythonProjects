import matplotlib.pyplot as plt

ano = list(range(2017, 2023))
nascimentos = [2677422, 2861250, 2846051, 2685103, 2686404, 2604734]
obitos = [1130654, 1231434, 1298282, 1492155, 1764118, 1493842]

plt.title('Nascimentos e Óbitos no Brasil (2017-2022)', fontsize=16)
plt.plot(ano, nascimentos, color='blue', label='Nascimentos')
plt.bar(ano, obitos, color='red', label='Óbitos')
plt.xlabel('Ano')
plt.ylabel('Números')
plt.grid()
plt.legend(fontsize=12)
plt.show()
