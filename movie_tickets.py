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
