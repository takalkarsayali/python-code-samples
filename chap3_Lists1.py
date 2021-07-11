#3.1 List of my friends
names = ["Sam","Akku","Bhavi",'Ruttya','Nik']
print(names[0])
print(names[1])
print(names[2])
print(names[-2])
print(names[-1])

#3.2 Greeting my friends in German
print('Heyy '+names[0]+' Gunten Morgen .Wie Ghets?')
print('Heyy '+names[1]+' Gunten Morgen .Wie Ghets?')
print('Heyy '+names[2]+' Gunten Morgen .Wie Ghets?')
print('Heyy '+names[3]+' Gunten Morgen .Wie Ghets?')

#3.3 in in chapt3_Lists.py

#3.4 List of three perons to invite them for dinner
persons=['A','B','C']
print('heyy! '+persons[0]+" you come at my place for dinner Today.")
print('heyy! '+persons[1]+" you come at my place for dinner Today.")
print('heyy! '+persons[2]+" you come at my place for dinner Today.")

#3.5 Changing the list
esc = persons.pop(2)
print(esc+" can't join wid u for dinner.")
print(persons)
persons.insert(3,'D')
print(persons)
print('Heyy! '+persons[0]+" you come at my place for dinner Today.")
print('Heyy! '+persons[1]+" you come at my place for dinner Today.")
print('Heyy! '+persons[2]+" you come at my place for dinner Today.")

#3.6 Adding more three people on the dinner table.
print("Heyy Guy's,some more friends are about to join us.")
persons.insert(0,"X")
persons.insert(3,"Y")
persons.insert(5,"Z")
persons.sort()
print(persons)
persons.sort(reverse=True)
print(persons)
print('Heyy! '+persons[0]+" you come at my place for dinner Today.")
print('Heyy! '+persons[1]+" you come at my place for dinner Today.")
print('Heyy! '+persons[2]+" you come at my place for dinner Today.")
print('Heyy! '+persons[3]+" you come at my place for dinner Today.")
print('Heyy! '+persons[4]+" you come at my place for dinner Today.")
print('Heyy! '+persons[5]+" you come at my place for dinner Today.")
print(len(persons))

#3.7 Shrinking the Guest list due unavilablabilty of sufficient space on dinner table
print("Sorry Guy's, I can't invite you all to the dinner because there is place for only 2 person.")
esc1=persons.pop(0)
print("Sorry "+esc1+" I can't invite you for dinner.")
esc2=persons.pop(-1)
print("Sorry "+esc2+" I can't invite you for dinner.")
esc3=persons.pop(1)
print("Sorry "+esc3+" I can't invite you for dinner.")
esc4=persons.pop(-2)
print("Sorry "+esc4+" I can't invite you for dinner.")
print(persons)
msg=persons[0] + " and "+ persons[1]+ " You are still invited for dinner."
print(msg)
del persons[1]
del persons[0]
print(persons)
print(len(persons))










