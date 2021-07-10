num = int(input("Enter a number: "))
for i in range(2,num):
    if num % i == 0:
        print("Composite")
        break

else:
    print("Prime")
    

