def gen(text):

    for w1 in text:
        yield w1
        


g = gen('abc')
print(g)
for i in g:
    print(f'Значение генератора: {i}')
print()