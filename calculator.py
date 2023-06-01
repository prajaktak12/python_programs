first_number = int(input(print("enter the first number")))

second_number = int(input(print("enter the second number")))

operator = input(print("enter the operator"))

if operator == '+':
    print( first_number + second_number)

if operator == '-':
    print(first_number - second_number)

if operator == '*':
    print(first_number * second_number)
  
if operator == '/':
    print(first_number / second_number)

else:
      print("please enter a valid operator")

