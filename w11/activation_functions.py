import matplotlib.pyplot as plt
#import seaborn; seaborn.set()
from numpy import exp, array, append

# Sigmoid activation function
def Sigmoid(x):
    return 1 / (1 + exp(-x))

# Graphical representation of our Sigmoid activation function
for i in array([range(-100, 100)]):
    x = append(array([]), i/10.0)
    plt.plot(x, Sigmoid(x))
    plt.title("Sigmoid activation function")
    plt.xlabel("x")
    plt.ylabel("S(x)")

plt.show()

# Tan-h activation function
def Tanh(x):
    return 2 / (1 + exp(-2*x)) - 1

# Graphical representation of our tan-h activation function
for i in array([range(-100, 100)]):
    x = append(array([]), i/10.0)
    plt.plot(x, Tanh(x))
    plt.title("Tan-h activation function")
    plt.xlabel("x")
    plt.ylabel("tanh(x)")

plt.show()
