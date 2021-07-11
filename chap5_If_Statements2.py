#5-8. Hello Admin:
persons=[]
if persons:
    for person in persons:
        print('Hello '+person+', thank you for logging in again.')
        if person =='Admin':
            print('would you like to see a status report?')
else:
    print('We need to find Some User.')


#5-10. Checking Usernames:
current_users=['Akhil','Bob','Canndy','Dumbo','Esha']
new_users=['BOB','Dumbo','Eshika','Giri','Akhil']
for new_user in new_users:
    if new_user in current_users:
        print(new_user+", This user name is already taken.\n # You will need to enter a new username.")
    else:
        print(new_user+', The user name is availabe.')

#5-11. Ordinal Numbers:
for nums in range(1,11):
    if nums == 1:
        print(str(nums)+"st")
    elif nums == 2:
        print(str(nums)+"nd")
    elif nums == 3:
        print(str(nums)+"rd")
    else:
        print(str(nums)+"th")

