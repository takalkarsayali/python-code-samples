# Assignment-04:
import math
#Accepting no. from user
a = int(input("Enter your number: "))
#Printing the Square of the number
print("Square:",a**2)
#Printing the Cube of the number
print("Cube:",a**3)
#Printing the Square-root of the number
print('Square Root:',math.sqrt(a))
#Printing the Factorial Value of the number
print('Factorial: ',math.factorial(a))
#To check weather the number is prime or compostie
if a == 1:
    print("The no. is neither prime nor composite.")
else:
    for i in range(2,a):
        if a % i == 0:
            print(str(a)+" is Composite number.")
            break
    else:
        print(str(a)+" is Prime number.")
#Printing the prime factors of the number
count = []
for num in range(2,a+1):
    if num>1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            while a%num == 0:
                count.append(num)
                a=a/num
print(count)

