class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return (f"Название: {self.name}; Этажность: {self.number_of_floors}")

    def __eq__(self, other):
        return self.number_of_floors == other

    def __lt__(self, other):
        pass

    def __le__(self, other):
       pass
    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __add__(self, other):
        if not isinstance(self.number_of_floors, int) or not isinstance(other, int):
            raise TypeError("Этажи должны быть целым числом!")
        return self.number_of_floors + other

    def __radd__(self, other):
        pass

    def __iadd__(self, other):
        return self.__add__(self, other)

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует!")
        else:
            print(f'Всего этажей: {self.number_of_floors}')
            for i in range(1, new_floor+1):
                print(f'Этаж: {i}')


h1 = House('Бурдж-Халифа', 163)
h2 = House('Куала-Лумпур', 118)

print(h1)
print(h2)

# __eq__
print(h1 == h2)

# __add__
h2 = h2 + 45
print(h1)
print(h2)
print(h1 == h2)

# __iadd__
h2 += 45
print(h2)
