import math
#function 1: fibonnaci sequence

def fibonacci(x):
    sum = 0

    if x == 1:
        return 0
    if x == 2:
        return 1
    else:
        a = 0
        b = 1
        for i in range (2,x):
            sum = a + b
            a = b
            b = sum
    return sum

#function 2: prime numbers

def is_prime(y):
    if y > 1:
        if y == 2:
            return True
        else:
            for i in range(2,int(y/2)+1):
                if (y % i) == 0:
                    return False
            return True   
    else:
        return False

            
#function 3: prime factorization

def print_prime_factors(n):
    print(n,"=",end=" ")
    if n == 2:
        print(n)
    else:
        while n % 2 == 0:
            print(2, end=" " if n%2 != 0 else " * ")
            n = n // 2
            
        for i in range(3,int(math.sqrt(n))+1,2):

            while n % i == 0:
                print(i, end=" " if (n%i) != 0 else " * ")
                n = n // i
                
        if n > 2:
            print(n)
