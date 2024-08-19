import random
# s1 = random.randint(3, 20)
# rand = 5
# password = str()

rand = random.randint(3, 20)

"""
    В одну строку склеивать такие две цифры, 
    которые в сумме кратны тому или иному числу
    в диапазоне от 
"""
if rand >= 3 and rand <= 20:
    password = ''
    # Индекс i в диапазоне от 1 до числа rand (1-ое слагаемое)
    for i in range(1, rand):
        # Индекс j в диапазоне от i++ до числа rand (2-ое слагаемое)
        for j in range(i + 1, rand):
            # Если остаток от деления на сумму индексов равен нулю:
            if rand % (i + j) == 0:
                password += str(i) + str(j)
    print(f'Пароль для числа {rand}: {password}')
else:
    print(f"Число не входит область допустимых значений")

# print(j)
# p = j+j+1
# p2 = rand % p
# print(p2)
# if p2 == 0:
#     print(p2)

# #if j < rand:
#     # print(j)
#     if rand % sum(rand, j):
#         print(j)

# print(f'Пароль для числа {rand}: {password}')
