#7-4 while loop asking user to asking his choice of pizza toppings
msg = ("(Enter 'done' when completed with the list.)")
msg += ("\nEnter the pizza toppings you want on your pizza: ")
toppings=""
while toppings != 'done':
    toppings = input(msg)

    if toppings != 'done':
        print(toppings+" added")
    else:
        print("Done with your pizza.")

# 7-5. Movie Tickets:
prompt = ("Enter your age: ")
prompt += ("\n(Enter 'quit' when you finish)")
while True:
    age = (input(prompt))
    if age == 'quit':
        break
    age == int(prompt)
    if age <= 3:
        print("Free Entry")
    elif age <=12:
        print("Pay $10 as the entry cost")
    else:
        print("\tPay $15 as a entry cost")


