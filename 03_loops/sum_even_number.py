n= int(input("enter a number:"))
sum_of_Even=0
for i in range(1,n+1):
    if (i%2==0):
        sum_of_Even+=i
    else:
        continue

print("the sum of even is",sum_of_Even)