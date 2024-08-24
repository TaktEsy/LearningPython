# def get_multiplied_digits(number):
#     str_number = str(number)
#     first = int(str_number[:1])
#
#     print("____________")
#     print("First", type(first))
#     print("First", type(first))
#
#     if str_number.__len__()>=1:
#         return first * get_multiplied_digits((int(str_number[1:])))
#     else:
#         return first
#
# result = get_multiplied_digits(40203)
# print(result)

def gmd(number):
    str_number = str(number)

    first = int(str_number[:1])
    f1 = len(str_number)

    if f1 == 0:
        return False
    else:
        print(first, type(first))
        return "Рекурсия: ", first * gmd(first-1)
    #
    #
    #
    #     return 0
    # else:
    #     s = int(str_number)
    #     return first * get_multiplied_digits(s-1)
    # print("____________")
    # print("First", type(first))
    # print("Str_number", type(str_number))

print(gmd(123))