#Programe to reverse the digits of the given number
#Accepting the number from the user and giving an idea what we gonna do with that number
msg = "Enter the number below and we'll return the reverse of that number.\nPlease Enter Positive Integer."
print(msg)
number = int(input("Enter the number: "))
reverse = 0
while number>0:
    remainder = number % 10
    reverse = (reverse*10) + remainder
    number = number // 10
print("Reverse of entered number is %d"%reverse)

