list1=[1,2,3,2,2]
list2=list1.copy()
list2.reverse()
print(list1)
print(list2)
if list1==list2:
    print("THIS IS A PALINDROME LIST")
else:
    print("NOT")