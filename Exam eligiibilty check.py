a=input("did you have medical causes? (yes/no): ")
if a=="yes":
    print("You are eligible for the exam.")
else:
    b=int(input("please enter your attendance: "))
    if b>=75:
        print("You are eligible for the exam.")
    else:
        print("You are not eligible for the exam.")
       