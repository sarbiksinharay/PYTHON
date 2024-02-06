num1=int(input("ENTER FIRST NUMBER:"))
num2=int(input("ENTER SECOND NUMBER:"))
opr=input("ENTER OPERATION:")
if (opr=='+'):
    print(num1,"+",num2,"=",num1+num2)
elif(opr=="-"):
    print(num1,"-",num2,"=",num1-num2)
elif(opr=="*"):
    print(num1,"*",num2,"=",num1*num2)
elif(opr=="/"):
    print(num1,"/",num2,"=",num1/num2)
elif(opr=="//"):
    print(num1,"//",num2,"=",num1//num2)
elif(opr=="**"):
    print(num1,"^",num2,"=",num1**num2)
elif(opr=="%"):
    print(num1,"%",num2,"=",num1%num2)
else:
    print("INVALID OPERATION")
