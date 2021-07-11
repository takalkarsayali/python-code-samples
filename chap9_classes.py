# 9-1/9-4: Restaurant:
class Restaurant():
    """ Discribing restaurnt in a class"""
    def __init__(self,restaurnt_name,cuisine_type):
        self.restaurnt_name = restaurnt_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print("Name of the restaurant is "+self.restaurnt_name.title()+'.')
        print("The type of cuisine is "+self.cuisine_type.title()+'.')
    def open_restaurant(self):
        print("The restaurant is now open.")
    def no_people_served(self):
        print("The number of people served by this restaurant is ",str(self.no_people_served()))

resto_1 = Restaurant("Taj Hotel",'Sea Food')
resto_1.describe_restaurant()
resto_1.open_restaurant()
resto_1.no_people_served()

print('\n')

resto_2 = Restaurant("Clove",'Italian')
resto_2.describe_restaurant()
resto_2.open_restaurant()

print('\n')
resto_3 = Restaurant("Cloud 9",'south indian')
resto_3.describe_restaurant()
resto_3.open_restaurant()

#9-2/9-3: User
class User():
    def __init__(self,first_name,last_name,username,email_Id,location):
        self.first_name = first_name
        self.last_name  = last_name
        self.username = username
        self.email_Id = email_Id
        self.location = location
    def describe_user(self):
        print(self.first_name.title()+" "+self.last_name.title())
        print("User name = "+self.username)
        print("Email Id = "+self.email_Id)
        print("Location = "+self.location.title())
    def greet_user(self):
        greet_msg = ("Welcome Back "+self.username+"!\nGlad to see you back:)")
        return greet_msg

print('\n')
user1 = User('Sayali',"Takalkar",'takalkarsayali','ab.c@gamil.com','pune')
user1.describe_user()
user1.greet_user()

# 9-5:

