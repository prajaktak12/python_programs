import numpy as my
z = my.arange(1,101)
print(z)

print(z.shape)
d = my.array([[1,2,3,4,5],[6,7,8,9,0]])
print(d.shape)

a = z.reshape(10,10)
print(a)

h = my.split(z,10)
print(h)

