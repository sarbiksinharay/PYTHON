num=12345
rem=0
sum_even=int(0)
sum_odd=int(0)
for i in range (0,5):
    rem=num%10
    num = num // 10

    if (rem % 2 == 0):
        sum_even += rem
    else:
        sum_odd += rem

print("sum even=",sum_even,"\nsum odd=",sum_odd)
