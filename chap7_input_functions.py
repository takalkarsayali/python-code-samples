#7-1 Rental Car :
car = input("What type of renatal car you would like look for: ")
print("Let me see if I can find you a "+car)

#7-2 Restuarant seating
member = int(input("How many people are there in your dinner group? "))
print("members = "+str(member))
if member >= 8:
    print("You'll have to wait for the table.\nTable for "+str(member)+" members is not availabe.")
else:
    print("Your table for "+str(member)+" members is ready.")

#7-3. Determining the multiples of Ten: 
num = int(input("Enter the number: "))
print(num)
if num % 10 == 0:
    print("Given number is multiple of 10.")
else:
    print("Given number is NOT the multiple of 10.")