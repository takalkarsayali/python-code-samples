#while loop asking user to asking his choice of pizza toppings
print("You will get the Pizza with your favourite toppings here.")
msg = ("(Enter 'done' when completed with the list.)")
msg += ("\nEnter the pizza toppings you want on your pizza: ")
toppings=""
while toppings != 'done':
    toppings = input(msg)

    if toppings != 'done':
        print(toppings+" added")
    else:
        print("Done with your pizza.")
