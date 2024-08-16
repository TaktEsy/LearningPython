from math import isqrt
from time import sleep

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
dl = 0
# for n in numbers:
#     for i in range(2, int(n**0.5) + 1):
#         print(n)
primes = []
not_primes = []
for n in numbers:
    if n == 1:
        print('Единица')
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                not_primes.append(n)
            else:
               primes.append(n)
print(primes)
print(not_primes)