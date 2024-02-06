number1=float(input("ENTER THE FIRST NUMBER:"))
number2=float(input("ENTER THE SECOND NUMBER:"))
number3=float(input("ENTER THE THIRD NUMBER:"))
if number1>number2 and number1>number3:
    print(number1,"IS GREATEST")
elif number2>number1 and  number2>number3:
    print(number2,"IS GREATEST")
else:
    print(number3,"IS GREATEST")
