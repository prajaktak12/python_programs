import numpy as my
arr=my.array([[[1,2,3,],[4,5,6],
                 [7,8,9],[10,11,12]]])
print(arr.ndim)

a = arr[0,1,1] + arr[0,1,2] 
print(a)