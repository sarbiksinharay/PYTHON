tup=(1,5,78,5,16,49)
search=100
present=0
i=0
while i<len(tup)-1:
     if tup[i]==search:
        present=1
        break
     i+=1

if(present==1):
   print(f"{search} present in tuple")
else:
    print(f"{search} not present in tuple")