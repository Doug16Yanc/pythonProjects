import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 500)
y = np.cumsum(np.random.randn(500, 6), 0)

plt.figure(figsize = (12, 7))
plt.plot(x, y)
plt.legend('ABCDEF', ncol = 2, loc = 'upper left')