name=input("ENTER YOUR NAME:")
if (name == "SARBIK" or name =="sarbik" or name=="Sarbik"):
   marks = int(input("ENTER YOUR MARKS:"))
   if  (marks >=90):
    print("YOU GOT A")
   elif (marks >=80):
    print("YOU GOT B")
   elif (marks >=70):
    print("YOU GOT C")
   else:
    print("NOT QUALIFIED")
else:
   print("WRONG INPUT")
print("\nTHANKYOU!!")