print("the percentage calculator")
a=float(input("Enter the english marks: "))
b=float(input("Enter the maths marks: "))
c=float(input("Enter the science marks: "))
d=float(input("Enter the french marks: "))
sum=a+b+c+d
print("the total marks is", sum)
percentage=(sum/400)*100
print("the percentage is",round(percentage, 2))
