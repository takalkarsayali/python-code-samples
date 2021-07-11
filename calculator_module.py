''' here are the functions for Calculator
    Calculator module
'''
'''
Merge Conflict test
'''
#1.Addition of two nos.
def add(x,y):
    print("The sum is : ", x+y)

#2.Subtraction of two nos.
def subtract(x,y):
    print("The difference is : ", x-y)

#3.Multiplication of two nos.
def multiply(x,y):
    print("The product is : ", x*y)

#4.Division of two nos.
def divide(x,y):
    if y == 0:
        print("Infinity")
    else:
        print("The Questiont is : ",x/y)
        print("The Remainder is : ",x % y)
    
#5.Area of Square
def sq_area(l):
    print('Area of square is :',l**2)

#6.Area of Rectangle
def rect_area(l,b):
    print('Area of Rectangel is :',l*b)

#7.Area of Triangle
def tri_area(b,h):
    print('Area of Triangle is : ',(b*h)/2)

#8.Area of Circle
def circle_area(r):
    print("Area of circle is : ",3.14*r**2)

#9.Area of semicircle
def semi_circle_area(r):
    print("Area of semi-circle is : ",(3.14*r**2)/2)

#10.Factorial
def fact(a):
    fact = 1
    for i in range(1,a+1):
        fact = fact*i
    print(str(a)+"! = ",fact)

#11. Square of the number
def square(a):
    print("Square of "+str(a)+" = ",a**2)

#12. Square root
def sq_root(a):
    print("Square Root of "+str(a)+" = ",a**0.5)

#13. Cube of the number
def cube(a):
    print("Cube of "+str(a)+" = ",a**3)

#14. Cube Root
def cube_root(a):
    print("Cube root of "+str(a)+" = ",a**0.33)