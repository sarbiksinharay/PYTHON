with open("practice.txt","r") as fl:
    data=fl.read()
    if data.find('learning')!= 0:
        print("exist")