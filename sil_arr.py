import numpy as my
v = my.array([23,56,856,46,35,856])

a = v.view()
v[5] = 0

print(a)
print(v)










