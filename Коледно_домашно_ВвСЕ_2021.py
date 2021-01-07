print("1. ")

def main():
    n = int(input('Find the next prime number greater great than: '))
    print (find_next_prime(n+1))

def find_next_prime(n):
    return find_prime_in_range(n, 2*n)

def find_prime_in_range(a, b):
    for p in range(a, b):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            return p
    return None

if __name__ == '__main__':
    main()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("2. ")

num = int(input())
rem = s = 0;
len = len(str(num))

n = num;

while (num > 0):
    rem = num % 10;
    s += int(rem ** len);
    num = num // 10;
    len -= 1;

if (s == n):
    print("disarium number");
else:
    print(" not a disarium number");

# import math
#
# def isPrime(n):
#
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#
#     for i in range(5, int(math.sqrt(n) + 1), 6):
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#
#     return True
#
# def nextPrime(N):
#     # Base case
#     if N <= 1:
#         return 2
#
#     prime = N
#     found = False
#
#     while (not found):
#         prime = prime + 1
#
#         if (isPrime(prime) == True):
#             found = True
#
#     return prime
#
# N = 3
# print(nextPrime(N))



# def prime(n):
#     n = int(input("Enter a number:"))
#     next_prime = n + 1
#     prime = True
#     while True:
#         for i in range(2, next_prime):
#             if next_prime % i == 0:
#                 prime = False
#                 break
#         if prime:
#             return next_prime
#         else:
#             next_prime = next_prime + 1
#             if next_prime % 2 == 0:
#                 next_prime = next_prime + 1
#             prime = True
#
#
# if __name__=="__main__":
#     print(prime(5))

# def prime(n):
#     np = []
#     isprime = []
#     for i in range(n+1, n+200):
#         np.append(i)
#     for j in np:
#         val_is_prime = True
#         for x in range(2, j-1):
#             if j % x == 0:
#                 val_is_prime = False
#                 break
#         if val_is_prime:
#             isprime.append(j)
#     return min(isprime)

# num = int(input("Input a number"))
#
# if num > 1:
#
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             print(i, "times", num // i, "is", num)
#             break
#     else:
#         print(num, "is a prime number")
#
# else:
#     print(num, "is not a prime number")
