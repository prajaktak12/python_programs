import numpy as f
from matplotlib import pyplot as plt

x = f.arange(1,13)
y = 1 * x + 1
plt.title("student marks")
plt.xlabel("name")
plt.ylabel("marks obtained")
plt.plot(x,y)
plt.show()