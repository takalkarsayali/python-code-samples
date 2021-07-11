# 4-1 Use for loop for the list of Pizzas
pizzas=[ 'Chicago Pizza','New York-Style Pizza','Sicilian Pizza','Greek Pizza']
for pizza in pizzas:
    print('I like '+ pizza+'.')
print("The types of Pizzas I like are 'Chicago','New York-Style','Sicilian'and 'Greek'Pizza.\nI really Love pizza.")

# 4-2 for loop in the list of animals
animals=['cat','dog','cow','horse']
for animal in animals:
    print(animal.title())
    print(animal.title()+' is a Domastic Animal.')
print("Any of these animals would make a great pet!")

# 4-3 First 20 numbers 
for x in range(1,21):
    print(x)

# 4-4/4-5 one million nos. with for loop
nums = list(range(1,1000000))
print(nums)
print(min(nums))
print(max(nums))
print(sum(nums))

# 4-6 Odd nos. form 1 to 20
for odd_nums in range(1,21,2):
    print(odd_nums)



    
