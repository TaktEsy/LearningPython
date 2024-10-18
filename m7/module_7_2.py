def custom_write(name, strs=None):
    lstr = []
    pstr = []
    with open(name, 'w', encoding='utf-8') as file:
        stroka = 0
        for s in strs:
            stroka += 1
            byte = file.tell()
            f = (stroka, byte)
            pstr.append(f)
            file.write(s + '\n')
            lstr.append(s)
        file.close()

    strings_positions = dict(zip(pstr, lstr))

    print(strings_positions)
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

custom_write('text.txt', strs=info)

print()