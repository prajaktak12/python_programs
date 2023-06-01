
from matplotlib import pyplot as plt


a=["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]

temp=[20,40,20,37,43,28,48,67,56,45,33,36]

plt.xlabel("months")
plt.ylabel("temperature")
plt.plot(a,temp)

plt.show()