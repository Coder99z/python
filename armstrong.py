a=int(input("enter a number of sum you want to find: "))
sum=0
b=a
while b>0:
    c=b%10
    sum+=c**3
    b=b//10

if a==sum:
    print("the number is armstrong number")
else:
    print("the number is not armstrong number")

