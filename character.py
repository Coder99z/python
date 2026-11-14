a=input("enter a word: ")
b=input("enter a character: ")
i=0
c=0
while i<len(a):
    if a[i]==b:
        c+=1
    i+=1
print("the character", b, "appears", c, "times in the word", a)