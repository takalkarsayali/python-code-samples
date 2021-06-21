#Creating a music album of users choice in the form of dictionary

def make_album(artist,album,tracks=0):    #defining a variable
    '''Build a album dictonary from users info'''
    album_dict = {
        'Artist':artist.title(),
        'Album':album.title()
    }
    if tracks:
        album_dict['Tracks']=tracks
    return album_dict
#Prompt msg display for user
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