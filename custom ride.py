print("select your ride")
print("1. Bike")
print("2. Car")
a=int(input("enter your choice: "))
if a==1:
    print("what type of bike:")
    print("1. Sports Bike")
    print("2. mountain Bike")
    b=int(input("enter your choice: "))
    if b==1:
        print("you have selected sports bike")
    else:
        print("you have selected mountain bike")
elif a==2:
    print("what type of car:")
    print("1. SUV")
    print("2. Sedan")
    c=int(input("enter your choice: "))
    if c==1:
        print("you have selected SUV")
    else:
        print("you have selected Sedan")
else:
    print("invalid choice")
