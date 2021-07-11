
#6.1 Person
persons_info={'first_name':'Sayali','last_name':'Takalkar','age':'19 years','city':'Pune'}
print(persons_info['first_name'])
print(persons_info['last_name'])
print(persons_info['age'])
print(persons_info['city'])

#6.1 person with loops
for key,value in persons_info.items():
    print("\nkey: "+ key)
    print("value: "+value)

#6.2 persons favourite numbers
fav_nos={'Sayali':'25','Sonal':'3','Atharva':'27','Archana':'2','Mahendra':'13'}
print("Sayali's favourite number is "+fav_nos['Sayali'])
print("Sonal's favourite number is "+fav_nos['Sonal'])
print("Atharva's favourite number is "+fav_nos['Atharva'])
print("Archana's favourite number is "+fav_nos['Archana'])
print("Mahendra's favourite number is "+fav_nos['Mahendra'])

#looping 6.2
for name, number in fav_nos.items():
    print("\n"+name+"'s favourite numbers is "+fav_nos[name])

#6.3/6.4:Glossary 1
#Dictonary of some programming words/funtions/methods with their meaning
prog_words={".title()":"Prints the out put in the Title formate.",
            ".upper()":"Prints the output in UpperCase.",
            ".lower()":"Prints the output in LowerCase.",
            "sorted()":"Sorts the output in the order",
            "print()":"Prints the content in pranthesis as output"
            }
for prog_word,function in prog_words.items():
    print("\n"+prog_word+":")
    print("       "+function)

#6.5 Rivers:Dictonary of the Rivers and its origin
Dict={"Indus":"Kailash",
      "Ganga":"Gangotri",
      "Krishana":"Mahabaleshwar",
      "Godavari":"Nasik Hills",
      "Brahmaputra":"Mansarover"
      }
for key,value in Dict.items():
    print("The "+key+" originates in "+value+".")
# printing the Rivers
for i in Dict.keys():
    print(i)
# printing the places
for j in Dict.values():
    print(j)

#6.6 Polling
favorite_languages = {'A':"Java",
                      'B':"C",
                      'C':"C++",
                      'D':'Python'
                      }
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +language.title() + ".")

peoples=['A','S','C','V','P','O','D']
for people in peoples:
    if people in favorite_languages:
        print(people+" Thanks for your response.")
    else:
        print(people+" U are invited to take poll.") 

# 6-7 Nested People's Dict
persons_info_1 = {'first_name':'Sayali',
                  'last_name':'Takalkar',
                  'age':'19 years',
                  'city':'Pune'}
persons_info_2 = {'first_name':'Sonal',
                  'last_name':'Takalkar',
                  'age':'17 years',
                  'city':'Pune'}
persons_info_3 = {'first_name':'Mrunali',
                  'last_name':'Padwal',
                  'age':'20 years',
                  'city':'Pune'}
people = [persons_info_1,persons_info_2,persons_info_3]
for person in people:
    print("\n")
    print(person)
    for key,value in person.items():
        print(key+':'+value)
        
# 6-8 Nested Pet's Dict
pet_1 = {'Owner':'Sayali',
           'Pet':'Horse'}
pet_2 = {'Owner':'Sonal',
           'Pet':'Dog'}
pet_3 = {'Owner':'Mrunali',
           'Pet':'Cat'}
pets = [pet_1,pet_2,pet_3]
for pet in pets:
    print("\n")
    print(pet)
    for Owner,Pet in pet.items():
        print(Owner+':'+Pet)

# 6-9 Nested Favourite places Dict
fav_place_1 = {'person':"Mrunali",
                "palce":'London'}
fav_place_2 = {'person':'Sonal',
                'place':'Paris'}
fav_place_3 = {'person':'Mati',
                'place':'Goa'}
fav_places = [fav_place_1,fav_place_2,fav_place_3]
print("\n")
for fav_place in fav_places:
    for person,place in fav_place.items():
        print(person+':'+place)

#6.10 Modifing Favourite nos.
fav_nos={'Sayali':['25','27','30'],
         'Sonal':['3','36','25','15'],
         'Atharva':['27'],
         'Archana':['2'],
         'Mahendra':['13']
         }
for name,fav_no in fav_nos.items():
    print("\n"+name+"'s favourite numbers are:")
    for numbers in fav_no:
        print("\t"+numbers)

print(fav_no.items())