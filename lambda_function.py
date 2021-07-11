#Lambda Function
#Eg.1
a = lambda a : a + 10
print(a(5))

#Eg.2
print('\n')
b = lambda a,b : a*b
print(b(2,5))

#Eg.3
print('\n')
x = lambda a,b,c : a + b + c
print(x(5,6,2))

#Eg.4 Use of lambda function
print("\n")
def myfunc(n):
    return lambda a : a*n
mydoubler = myfunc(2)
mytriple = myfunc(3)
print(mydoubler(11))
print(mytriple(11))

x = lambda a:a
print(x(2))