import numpy as pr
a=pr.arange(1,101)
print(a)

print(a.shape)
b=pr.array([[2,3,4,5,56,6],[4,5,6,78,8,9]])
print(b.shape)

n=a.reshape(10,10)
print(n)

f=pr.split(a,10)
print(f)