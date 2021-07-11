def tri_recursion(k):
    if(k>0):          # value of k goes from 1 to k(6 in this eg.)
        result = k + tri_recursion(k-1)     # result = 1+(1-1) = 1+0 = 1
        print(result)
    else:                                    # similarly 
        result = 0                           # result = 2+(2-1)=3                
    return result
    
print("Recursion example result")
tri_recursion(3)    

