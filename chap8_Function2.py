#8-9 Magicians
def show_magicians():

    for magician in magicians:
        print(magician)
    
magicians = ['A','B','C']
print("The magicians are: \n")
show_magicians()

print('\n')
#8-10 Great Magicians
def make_greet():
    for magician in magicians:
        print(magician+":The Great Magician ")
make_greet()

print('\n')
#8-12 Sandwich
print("Making sandwich with following items:")
def sandwich(*items):
    for item in items:
        print('- '+item)

sandwich("Bread",'dwerd')
sandwich("Cheese","Tomato")
sandwich('Qading','dsfwfv','jnshgya','sdbybkhf')


print("\n")
# 8-13 User Profile
def build_profile(first,last,**user_info):
    '''Build a dictionary containing everything we know about a user.'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Sayali','Takalkar',age='18')
print(user_profile)

print('\n')
# 8-14 Cars
def make_car(manufacturer,model_name,**car_info):
    '''Build a dictionary containing everything we know about a car.'''
    car = {}
    car["Manufacturer"] = manufacturer.title()
    car['Model name'] = model_name.title()
    for key,value in car_info.items():
        car[key.title()] = value.title()
    return car 

car_info = make_car('TATA','Nexon',colour='Blue')
print(car_info)

print('\n')

