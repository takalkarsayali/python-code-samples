a = int(input('Enter the number:'))
count = []
for num in range(2,a+1):
    if num>1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            while a%num == 0:
                count.append(num)
                a=a/num
print(count)