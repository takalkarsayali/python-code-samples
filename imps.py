a="Sameer"
b=18
c=3.14
print("%s is %d yrs old and value of PI is %f."%(a,b,c))

print(format(432002984787,',')) 
print (format(16/3,'.6f'))
a=0
b=5
x=(a&b)|(a&a)|(a|b)
print(x)

a=7
b=6
x=a | b
print(x)


n = int(input("Enter range:"))
print(*range(1,n+1),sep='')