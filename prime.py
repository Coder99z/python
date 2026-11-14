l=int(input("enter a lower range:"))
h=int(input("enter a higher range:"))
print("prime numbers between",l,"and",h,"are:")
for num in range(l,h+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)