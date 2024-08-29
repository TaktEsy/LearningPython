data = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
num_sum = 0
len_sum = 0

def sum_len(*args):
    global num_sum, len_sum
    args_len = args.__len__()
    print(f"==========================")
    print(f"Полученные данные: {args}")
    print(f"Кол-во элементов: {len(args)}")
    print(f"-------")

    for i in args:
        print(f"Что в работе: {i}")

        if type(i).__name__ == 'int':
            print(f'Число: {i}')
            print(f"-------")
            num_sum += i
        elif isinstance(i, str):
            print(f'Строка: {i}')
            print(f"-------")
            len_sum += len(i)
        else:
            print(f'Элемент с элементами: {i}')
            print(f"-------")
            if len(i) > 0:
                return sum_len(i[0])

    print(f"=========================")
print(sum_len(data))


# def sum_len(*args):
#     global num_sum, len_sum
#     print(f"Данные на входе {args}")
#     args_len = args.__len__()
#
#
#     for i in args:
#         if args_len > 0:
#             if type(i).__name__ == 'int':
#                 num_sum += i
#
#
#             elif isinstance(i, str):
#                 len_sum += len(i)
#
#             # elif isinstance(i, dict):
#             #     print(f"{i} -  Словарь! Идем дальше...")
#             #     for k in i:
#             #         print(f"{k} - Элемент", type(k))
#             #         len_sum += len(k)
#             else:
#                 for k in i:
#                     print(f"{i} -  Не строка и не число! Идем дальше...")
#                     print(f"{k} - Элемент", type(k))
#
#
#
#
#         print(f"Сумма всех чисел: {num_sum}")
#         print(f"Сумма длин всех строк: {len_sum}")
#         print("---------------------------------------")


    # while args_len > 0:
    #     print(args)
    #     if type(args).__name__ == 'int':
    #         print("FFFFFa")
    #     elif isinstance(args, str):
    #         print(args)
    #     else:
    #         return sum_len[]
    #     args_len -= 1
    #     break
    # else:
    #     print("Отсутствуют данные!")

    # # while args_len:
    # print(type(args))
    # args_len = len(args)
    # while args.__len__() > 0:
    #
    # else:
    #     print("Отсутствуют данные!")
    #     return False