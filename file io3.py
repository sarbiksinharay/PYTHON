count_e,count_o=0,0
with open("practice.txt","r") as fl:
    data=fl.read()
    nums=data.split(",")
    print(data)
    for i in nums:
        if(int(i)%2==0):
            count_e+=1
        else:
            count_o+=1        
            
print("Even Numbers:",count_e,"\nOdd Numbers:",count_o)            