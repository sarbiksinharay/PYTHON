with open("practice.txt","r") as fl:
    data=fl.read()
    print("Before:\n",data)
    new_data=data.replace("java","Python")
    
with open("practice.txt","w") as fl:
    fl.write(new_data)
    print("After:\n",new_data)