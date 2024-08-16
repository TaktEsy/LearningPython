"""
Задача "Всё не так уж просто":
Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Используя этот список составьте второй список primes содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).

Вывод на консоль:
Primes: [2, 3, 5, 7, 11, 13]
Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]
"""
import math
from time import sleep

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = None
div = 2

for n in numbers:
    if n == 1:
        print('Единица')
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                not_primes.append(n)
            else:
               primes.append(n)
    # else:
    #     for divr in range(2, int(n**0.5 + 1)):
    #         if n % divr == 0:
    #             is_prime = False
    #             not_primes.append(n)
    #             break
    #         else:
    #             is_prime = True
    #             primes.append(n)


    # if n in range(2, n):
    #     print(f"Простое число: {n}")
    # if i >= 2:
    #     number_sqrt = int(math.sqrt(i))
    #     print(number_sqrt)

print(numbers)
print(f'Составные числа: {primes}')
print(f'Простые числа: {not_primes}')
