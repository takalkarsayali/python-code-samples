#String operations
#Asking for the string
string1 = input("Enter the string:")

#Printing the length of the string
length = int(len(string1))
print("Length of the string is",length)
#String Reversal
reversal = ''
i = 0
while i>(-length):
    i = i-1
    reversal = reversal+string1[i]
print(reversal)

#Checking the condition for palindrome 
if reversal.lower() == string1.lower():
    print("Palindrome")
else:
    print("Not palindrome")

#Checking sub-string
sub_string = input("Enter the substring:")
if sub_string in string1:
    print("True")
else:
    print("False")

#checking the equality between to strings
string2 = input("Enter another string to compare:")
if string1 == string2:
    print("Strings are equal.")
else:
    print("Strings are not equal.")
