def custom_write(name, strs=None):
    with open(name, 'w') as file:
        for s in strs:
            file.write(s + '\n')
        file.close()


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

custom_write('text.txt', strs=info)

print()