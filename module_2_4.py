"""
Задача "Всё не так уж просто":
Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Используя этот список составьте второй список primes содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).

Вывод на консоль:
Primes: [2, 3, 5, 7, 11, 13]
Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]

Натуральное число, большее 1, называется простым, если оно ни на что не делится, кроме себя и 1

Пункты задачи:
1. Создайте пустые списки primes и not_primes.
2. При помощи цикла for переберите список numbers.
3. Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
4. Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
5. В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
6. Выведите списки primes и not_primes на экран(в консоль).
"""
import math

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = None
div = 2

# Цикл для перебора списка с данными
for n in numbers:
    # Сразу отметаем единицу т.к. она не является простым числом
    if n != 1:
        print(f'{n}')
        sq = math.sqrt(n)
        for i in range(2, sq + 1):
            if n % i == 0:
                not_primes.append(n)
            else:
               primes.append(n)
    else:
        print('')

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

# print(numbers)
# print(f'Составные числа: {primes}')
# print(f'Простые числа: {not_primes}')
