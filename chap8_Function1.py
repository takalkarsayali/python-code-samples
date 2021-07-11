# 8-1 Message:Telling what are we learning in this chapter no.8 'Function'
def display_message():
    '''will display what we will learn in this chapter'''
    print("We will learn Functions in this chapter.")
display_message()

print('\n')
# 8-2 My favourite book
def favourite_book(title):
    '''Displays the title of the book'''
    print("One of my favourite book is "+title.title()+".")
favourite_book('the kirshna key')

print('\n')
# 8-3 T-shirts
def make_shirt(size,text_msg):
    '''prints the shirt as per given size and text msg'''
    print("The T-shirt of size "+str(size)+" inch with the print message '"+text_msg+"' is ready.")
make_shirt(91,'Hello World')

print('\n')
# 8-4 Large-shirts
def make_shirt(size,text_msg="I Love Python"):
    '''prints the shirt as per given size and text msg'''
    print("The T-shirt of size "+str(size)+" size with the print message '"+text_msg+"' is ready.")
make_shirt("'large'")
make_shirt("'medium'")
make_shirt("'random'","I also Love C++")

print('\n')
#8-5 cities
def describe_cities(city,country='India'):
    '''Will tell the city and its country'''
    print(city.title()+' is in '+country.title())
describe_cities('Pune')
describe_cities('goa')
describe_cities('london','england')

print('\n')
# 8-6 City-country pair using return function
def city_country(city, country):
    """City-country pair using return function"""
    return ('"'+city.title()+','+country.title()+'"')
city_1 = city_country("Pune","India")
print(city_1)
city_2 = city_country("Mumbai","India")
print(city_2)
city_3 = city_country("Goa","India")
print(city_3)

print('\n')
# 8-7 Album
def make_album(artist,album_title,tracks=""):
    '''Return the name of artist and his album in the form of dictionary'''
    if tracks:                                                                  # code form this line onwards is written in another formate at line no.76. 
        dict = {'Artist':artist,"Album":album_title,'tracks':tracks}
    else:
        dict = {'Artist':artist,"Album":album_title}
    return (dict)
dict_1 = make_album('Dhanvi','Vaaste',5)
print(dict_1)
dict_2 = make_album('Sonu Nigam','Agneepath')
print(dict_2)
dict_3 = make_album('Arman Malik','Buttabooma')
print(dict_3)
                                    
print('\n')
print("\t")
# 8-8:Users Album
def make_album(artist,album,tracks=0):    
    '''Build a album dictonary from users info'''
    album_dict = {
        'Artist':artist.title(),
        'Album':album.title()
    }
    if tracks:
        album_dict['Tracks']=tracks
    return album_dict
print("[Enter 'quit' whene you want to stop]")
prompt_artist = 'Enter the name of the artist: '
prompt_album = 'Enter the name of his album: '
while True:
    artist = input(prompt_artist)
    if artist == 'quit':
        break
    album = input(prompt_album)
    if album == 'quit':
        break
    album = make_album(artist,album)
    print(album)
print("\n\tThanks for responding.")


