num=input("ENTER A NUMBER:")
if num.isdigit():
   for i in range (1,11):
       print(int(num)," x ",int(i),"=",int(i)*int(num))
else:
    print("WRONG INPUT")