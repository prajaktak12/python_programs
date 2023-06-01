# Import libraries
from matplotlib import pyplot as plt
import numpy as np
 
cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR', 'MERCEDES']
 
data = [23, 17, 35, 29, 12, 41]

myexplode=[0.2, 0, 0, 0,0,0]
plt.figure(figsize=(7, 7))
plt.pie(data, labels = cars,autopct="%1.2f",explode=myexplode)
plt.legend(loc="lower right",ncol=1)
plt.title("car names")
 

plt.show()