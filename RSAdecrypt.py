import math

def factors(number):
    f =[(x, number / x)  for x in range(int(math.sqrt(number)))[2:] if not number % x]
    return f

def RSA_decyrpt(c,e,n):
    p=factors(n[0])
    q=factors(n[1])
    n= p*q
    phi= (p-1)*(q-1)
    #d=(libnum.invmod(e,phi))
    result= c**d % n
    return result

print()
   

