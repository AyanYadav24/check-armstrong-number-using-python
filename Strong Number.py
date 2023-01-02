import math
def strong_num(a):
    total=0
    for i in range(0,len(a)):
        total+=math.factorial(int(a[i]))
    if total==int(a):
        return("STRONG NUMBER")
    else:
        return("NOT A strong NUMBER")
a=input("enter the number: ")
print(strong_num(a))
