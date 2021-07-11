#Assignment 2:Operations on n terms
my_list = []
n = int(input("Enter the total no. of elements in the list: "))

for i in range(0,n):
    a = float(input("Enter the no."))
    my_list.append(a)

max = max(my_list)
min = min(my_list)
sum = sum(my_list)
avg = sum/len(my_list)

print("Maximum of the numbers is ",max)
print("Minimun of the numbers is ",min)
print("Sum of the numbers is ",sum)
print("Average value of the numbers is ",avg)

