import random
import math
import sys
import time 

def rabinMiller(n):
     s = n-1
     t = 0
     while s&1 == 0:
         s = s/2
         t +=1
     k = 0
     while k<128:
         a = random.randrange(2,n-1)
         v = pow(a,s,n) 
         if v != 1:
             i=0
             while v != (n-1):
                 if i == t-1:
                     return False
                 else:
                     i = i+1
                     v = (v**2)%n
         k+=2
     return True

def isPrime(n):
     lowPrimes =   [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
                   ,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179
                   ,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269
                   ,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367
                   ,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461
                   ,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571
                   ,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661
                   ,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773
                   ,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883
                   ,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
     if (n >= 3):
         if (n&1 != 0):
             for p in lowPrimes:
                 if (n == p):
                    return True
                 if (n % p == 0):
                     return False
             return rabinMiller(n)
     return False

def generateLargePrime(k):
     r=100*(math.log(k,2)+1) 
     r_ = r
     while r>0:
         n = random.randrange(2**(k-1),2**(k))
         r-=1
         if isPrime(n) == True:
             return n
     return "Failure after "+`r_` + " tries."

prime1 = generateLargePrime(512)
prime2 = generateLargePrime(512)
prime3 = generateLargePrime(512)

def returnvalue(p, q):
    return p * q

def ab(p, q):
     a = p - 1
     b = q - 1
     c = a * b
     return c

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
def GCD(p, q):
    a = p - 1
    b = q - 1
    r = a % b
    if r != 0:
        return GCD(b, r)
    return b

def modpow(num, pow, mod):
    test = 1
    n = num
    while pow:
        pow = pow >> 1
        if pow & 1:
            test = ((test % mod) * (n % mod)) % mod
            n = ((n % mod) * (n % mod)) % mod
    return test

nvalue = returnvalue(prime1,prime2)
evalue = prime3
combine = ab(prime1,prime2)
LCM = ab(prime1,prime2) / GCD (prime1,prime2)
inverse = modinv(evalue,LCM)
plaintext = 666970535767547056526570696849515566556557676649706868694956577056565167536968676554565651507052556553575652576969676755515249
encrypt = modpow(plaintext, evalue, nvalue)
print("The encrypted text is", encrypt)
print("The first prime number is", prime1)
print("The second prime number is", prime2)
