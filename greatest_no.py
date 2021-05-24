# Accepting three values from the user
x=int(input("Enter 1st number: "))
y=int(input("Enter 2nd number: "))
z=int(input("Enter 3rd number: "))
#condtion for x as a greatest number
if(x>y) and (x>z):
    L=x
    print('The largest number is',L)
#condtion for y as a greatest number
elif (y>x) and (y>z):
    L=y
    print('The greatest number is',L)
#condtion for z as a greatest number
else:
    L=z
    print('The largest number is',L)