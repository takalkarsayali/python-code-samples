x=int(input("Enter 1st number: "))
y=int(input("Enter 2nd number: "))
z=int(input("Enter 3rd number: "))
if(x>y) and (x>z):
    L=x
    print('The largest number is',L)
elif (y>x) and (y>z):
    L=y
    print('The largest number is',L)
else:
    L=z
    print('The largest number is',L)