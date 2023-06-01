import numpy as h
from matplotlib import pyplot as pyt

country = ["India","USA","Russia","UAE","Bangladesh"]

data = ["30","34","67","40","25"]

pyt.title("popualtion worldwide")
pyt.pie(data,labels = country ,autopct = "%1.0f")
pyt.legend(title = "note : population in lakhs" ,ncol = 1,loc ="upper left")
pyt.plot()
pyt.show()