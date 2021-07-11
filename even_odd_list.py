#To seperate the list of elements in Even and Odd list
n = int(input("Enter the number of elements:"))
list = []
for i in range(1,n+1):
    a = int(input("Enter the element:"))
    list.append(a)
print("List = "+str(list))
even_list = []
odd_list = []
for j in list:
    if j%2==0:
        even_list.append(j)
    else:
        odd_list.append(j)
print('Even list = '+str(even_list))
if len(even_list)==1:
    print(str(len(even_list)),"Even element.")
else:
    print(str(len(even_list)),"Even elements.")

print('Odd list = '+str(odd_list))
if len(odd_list)==1:
    print(str(len(odd_list)),"Odd element.")
else:
    print(str(len(odd_list)),"Odd elements.")
