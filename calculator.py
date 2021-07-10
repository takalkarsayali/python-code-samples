# A Calculator
from calculator_module import*
#Asking for the operation to be performed
print("Which operation do you want to perform ?\n 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Area of Square\n 6.Area of Rectangle\n 7.Area of Triangle\n 8.Area of a Circle\n 9.Area of a Semi-circle\n 10.Factorial\n 11.Square of the number\n 12.Square root of the number\n 13.Cube of the number\n 14.Cube root of the number\n")
#Asking for the choice no.
choice = int(input("Enter your choice number: "))
print("\n")
if choice == 1:
    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))
    add(a,b)
elif choice == 2:
    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))
    subtract(a,b)
elif choice == 3:
    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))
    multiply(a,b)
elif choice == 4:
    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))
    divide(a,b)
elif choice == 5:
    l = float(input("Enter the length of the Square: "))
    sq_area(l)
elif choice == 6:
    l = float(input("Enter the length of the rectangle: "))
    b = float(input("Enter the breadth of the rectangle: "))
    rect_area(l,b)
elif choice == 7:
    b = float(input("Enter the base of the triangle: "))
    h = float(input("Enter the height of the triangle: "))
    tri_area(b,h)
elif choice == 8:
    r = float(input("Enter the radius of the circle: "))
    circle_area(r)
elif choice == 9:
    r = float(input("Enter the radius of the semi-circle: "))
    semi_circle_area(r)
elif choice == 10:
    a = int(input('Enter the number: '))
    fact(a)
elif choice == 11:
    a = int(input("Enter the number:"))
    square(a)
elif choice == 12:
    a = int(input("Enter the number:"))
    sq_root(a)
elif choice == 13:
    a = int(input("Enter the number:"))
    cube(a)
elif choice == 14:
    a = int(input("Enter the number:"))
    cube_root(a)

print('\nThank You:)')
  
    
