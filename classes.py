class Dog():
    """A simple attempt to modeal a dog."""
    def __init__(self,name,age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title()+" is now sitting.")
    def roll_over(self):
        """Simulate rolling over in respons to a command."""
        print(self.name.title()+" rolled over!")

my_dog = Dog('willie',6)
print("My dog's name is "+my_dog.name.title()+'.')
print("My dog is "+str(my_dog.age)+' years old.')
my_dog.sit()

print('\n')
your_dog = Dog('lucky',6)
print("Your dog's name is "+your_dog.name.title()+'.')
print("Your dog is "+str(your_dog.age)+' years old.')
your_dog.roll_over()
