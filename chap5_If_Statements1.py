#5-3. Alien Colors#1
alien_colours=['Red','Yellow','Green']
if 'Green' in alien_colours:
    print("The player earned 5 points.")
if 'Pink' in alien_colours:
    print('U won.')
if 'Red'in alien_colours:
    print('Oh!U losed.')

#5-4.Alien Colours#2
if 'Green' in alien_colours:
    print("You earned 5 points for shooting the alien.")
else:
    print("U earned 10 points.")

#5-5.Alien Colours#3
if 'Green' in alien_colours:
    print("You earned 5 points.")
elif 'Yellow' in alien_colours:
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

#5-6. Stages of Life:
age=int(input('Enter Your Age:'))
# If the person is less than 2 years old, print a message that the person is a baby.
if age<2:
    print('You are in babies category.')
#If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
elif age>=2 or age<4:
    print('You are in toddler category.')
# If the person is at least 4 years old but less than 13, print a message that the person is a kid.
elif age>=4 or age<13:
    print('You are in kids category.')
#If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
elif age>=13 or age<20:
    print('You are in teenager category.')
#If the person is at least 20 years old but less than 65, print a message that the person is an adult.
elif age>=20 or age<65:
    print('You are in adult category.')
#If the person is age 65 or older, print a message that the person is an elder.
elif age>65:
    print('You are in elder category.')

#5-7. Favorite Fruit: 
fav_fruit=['Apple','Mango','Banana','Pineapple']
if 'Apple' in fav_fruit:
    print('You really like Apple.')
if 'Banana' in fav_fruit:
    print('You really like Banana.')   
if 'Strawberries' in fav_fruit:
    print('You really like Strawberries.')