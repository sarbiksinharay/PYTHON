with open("practice.txt","r") as fl:
    data=True
    line_n=1
    while data:
        data=fl.readline()
        if data.find('learning')!=-1:
            print(line_n)
        line_n+=1    