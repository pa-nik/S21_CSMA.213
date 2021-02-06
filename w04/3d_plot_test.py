import numpy as np
import matplotlib.pyplot as plt
import math
import random


def f(x, y):
    # return np.sin(np.sqrt(x ** 2 + y ** 2))
    return (x + 2 * y - 7)**2 + (2 * x + y - 5)**2

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
# ax.set_title('surface')
ax.set_title('(x + 2 * y - 7)**2 + (2 * x + y - 5)**2')
plt.show()