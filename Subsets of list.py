lst=[1,2,3]
subsets=[[]]
n=len(lst)
for element in lst:
    n_subsets=[]
    for subset in subsets:
       n_subset=subset+[element]
       n_subsets.append(n_subset)
    subsets.extend(n_subsets)
print(subsets)