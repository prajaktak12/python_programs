from matplotlib import pyplot as pyt

a = ["2015","2016","2017","2019","2020","2021"]

price = [50,51,57,54,57,60]
pyt.xlabel("years")
pyt.ylabel("price")
pyt.plot(a,price)
pyt.title("price in lakhs")

pyt.show()