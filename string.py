a = "hello"
print(a)

b = """we can print long sentences using
trpile inverted comas and we can save then as variables"""
print(b)

#slicing string
print(b[2:10])

print(b[:11])


#modifying
print(a.lower())

print(b.upper())

print(b.replace("we","i"))

print(b.split("and"))

#concatenation
print(a+b)

#string formating
age = 30
quantity = 10
text = "my name is prajakta and i am  10 years old"
print(text.format(age))

quantity = 6
iteam = 500
price =  678.45
myorder = "i am buying {2} with quantity {1} and paying {0}"
print(myorder.format(price,quantity,iteam))

