# Домашняя работа по уроку "Функции в Python.Функция с параметром"
# Задача "Матрица воплоти":
"""
    Пункты задачи:
    Объявите функцию get_matrix и напишите в ней параметры n, m и value.
    Создайте пустой список matrix внутри функции get_matrix.
    Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
    В первом цикле добавляйте пустой список в список matrix.
    Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
    Во втором цикле пополняйте ранее добавленный пустой список значениями value.
    После всех циклов верните значение переменной matrix.
    Выведите на экран(консоль) результат работы функции get_matrix.
"""
"""
    Пример результата выполнения функции:
    Исходный код:
    result1 = get_matrix(2, 2, 10)
    result2 = get_matrix(3, 5, 42)
    result3 = get_matrix(4, 2, 13)
    print(result1)
    print(result2)
    print(result3)
"""
def get_matrix(n,m,value):
    # Сама матрица
    matrix = []
    print(f'Кол-во строк: {n}; Кол-во столбцов: {m}; Значения: {value}')
    if n != 0 and m != 0:
        for w in range(0, n):
            matrix.append(list())
            # print(w)
            for r in range(0, m):
                matrix[w].append(value)
                print(r)
    else:
        print('Создание нулевой матрицы недопустимо')
        return False
    return matrix

print("Результат функции: ", get_matrix(2,2,10))
