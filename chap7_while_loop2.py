# 7-8:Deli
sandwich_orders = ["veggie",'Cheese grill','roasted beef','tuna']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm Working on your "+current_sandwich+" sandwich")
    finished_sandwiches.append(current_sandwich)
print("\n")
for sandwich in finished_sandwiches:
    print("I made your "+sandwich+" sandwich")

#7-8 . No Pastrami:
sandwich_orders = ["veggie",'Pastrami','Cheese grill','Pastrami','roasted beef','Pastrami','tuna']
finished_sandwiches=[]
print(sandwich_orders)
print("Pastrami out of range")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
print('\n')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I am working on your "+current_sandwich+" sandwich")
    finished_sandwiches.append(current_sandwich.title())
print("\n")
for sandwich in finished_sandwiches:
    print("I made Your "+sandwich+" sandwich ")

    
print("\n")
# 7-10 Dream Vacation:
prompt = ("(Enter 'quit' when done)")
prompt += ("\nIf you could visit one place in the world, where would you go?")
while True:
    place = input(prompt)
    if place == 'quit':
        break
    else:
        print(place)

