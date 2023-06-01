import numpy as np 
from matplotlib import pyplot as plt 

a=np.arange(1,20)
b=np.arange(1,20)
plt.title("example") 
plt.xlabel("student") 
plt.ylabel("percentage") 
plt.plot(a,b,"o") 
plt.show()