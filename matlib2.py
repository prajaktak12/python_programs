import numpy as h
from matplotlib import pyplot as pyt

gases = ["oxygen","carbon dioxide","nitrogen","argon","other gases"]

data = ["21","3","71","4","3"]

pyt.title("composition of atmosphere")
pyt.pie(data,labels = gases ,autopct = "%1.1f")
pyt.legend(title = "scale",loc = "lower left",ncol = 2 )
pyt.plot()
pyt.show()