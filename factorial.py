# To find the factorial of any number

print("To find Factorial of given number.")
num = int(input("Enter a no.: "))
fact = 1
for i in range(1,num+1):
    fact = fact*i
print(str(num)+"! = "+str(fact))