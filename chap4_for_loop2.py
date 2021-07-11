#4-7 nos. divisible by 3
l=[i for i in range (3,31) if i % 3 == 0]
print(l)
# another way for printing the same result
l=[]
for x in range(3,31):
    if x % 3 == 0:
        l.append(x)
print(l)

#4-8 cube of first ten numbers
for i in range(1,11):
    print(i**3)
#another way
for i in range(1,11):
    x = i ** 3
    print(x)

#4-9 list of first 10 cubes
cubes=[i**3 for i in range(1,11)]
print(cubes) 
# Another Method
cubes=[]
for i in range(1,11):
    cubes.append(i**3)
print(cubes)

#4-10 slicing list
print('First three numbers in the list are:')
print(cubes[:3])
print('Three numbers from the middle of the list are:')
print(cubes[4:7])
print('Three numbers at the last are:')
print(cubes[7:])

#4-11 My and my friends favourite Pizzas
my_pizzas=[ 'Chicago Pizza','New York-Style Pizza','Sicilian Pizza','Greek Pizza']
friend_pizzas=my_pizzas[:]
my_pizzas.append("Chesse Italian Pizza")
friend_pizzas.append("Chicken Pizza")
print(my_pizzas)
print(friend_pizzas)
print('My Favourite Pizzas are ')
print(my_pizzas)
print('My Friends Favourite Pizzas are')
print(friend_pizzas)

#4.12 more Loops
my_foods = ['pizza', 'falafel', 'carrot cake']
for food in my_foods:
    print(food)