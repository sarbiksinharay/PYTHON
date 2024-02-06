num1=int(input("ENTER FIRST NUMBER:"))
if (num1==0):
        print("0 IS NEUTRAL NUMBER")


elif (num1%2==0):
    if(num1<0):
        print(num1,"IS EVEN NEGATIVE NUMBER")
    else:
        print(num1, "IS EVEN POSITIVE NUMBER")
else:
    if (num1 < 0):
        print(num1, "IS ODD NEGATIVE NUMBER")
    else:
        print(num1, "IS ODD POSITIVE NUMBER")