def calculator(x,y):
    sum=x+y
    sub=x-y
    mul=x*y
    div=x/y
    mod=x%y
    print(x,"+",y,"=",sum)
    print(x,"-",y,"=",sub)
    print(x,"x",y,"=",mul)
    print(x,"/",y,"=",div)
    print(x,"%",y,"=",mod)

num1=int(input("ENTER THE FIRST NUMBER:"))
num2=int(input("ENTER THE SECOND NUMBER:"))
calculator(num1,num2)