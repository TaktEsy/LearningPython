"""
Задача "Всё не так уж просто":
Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Используя этот список составьте второй список primes содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).
"""
import math

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
div = 2

for n in numbers:
    if -1 <= n <= 1:
        is_prime = False
        continue
    else:
        while div ** 2 <= n and is_prime is True:
            if n % div == 0:
                is_prime = False
            else:
                div += 1
    if is_prime is True:
        print(n)

    # if n in range(2, n):
    #     print(f"Простое число: {n}")
    # if i >= 2:
    #     number_sqrt = int(math.sqrt(i))
    #     print(number_sqrt)

print(numbers)
print(primes)
print(not_primes)