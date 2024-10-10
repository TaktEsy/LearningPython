from math import *

class Figure:
    SIDES_COUNT = 0
    __sides: list
    __color: list
    filled: bool
    s: bool

    # Магия
    def __init__(self, color, *sides):
        self.__sides = list(sides)
        self.__color = list(color)

    def __len__(self):
        return sum(self.__sides)

    # Валидаторы
    def __is_valid_color(self, r, g, b):
        if r not in range(0, 256):
            raise ("Incorrect R")
        elif g not in range(0, 255):
            raise ("Incorrect RGB")
        elif b not in range(0, 255):
            raise ("Incorrect RGB")
        else:
            return True

    def __is_valid_sides(self, *args):
        args = list(*args)
        if len(args) == self.SIDES_COUNT:
            return True

    # Сеттеры
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides
        else:
            i = 0
            default_sides = []
            while i < self.SIDES_COUNT:
                default_sides.append(1)
                i+=1
            self.__sides = default_sides
            # print(self.__sides)
            # i=0
            # while i <= self.SIDES_COUNT:
            #     self.__sides[i] = 1
            #     i+=1

    # Геттеры
    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides




class Circle(Figure):
    SIDES_COUNT = 1
    __radius: float

    def __init__(self, color, *sides):

        super().__init__(color, *sides)


class Triangle(Figure):
    SIDES_COUNT = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        s = super().get_sides()
        a = float(s[0])
        b = float(s[1])
        c = float(s[2])

        p = float(super().__len__()) / 2.0 # Полупериметр
        area = sqrt(p*abs(p-a)*abs(p-b)*abs(p-c))

        return area

class Cube(Figure):
    SIDES_COUNT = 12
    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_volume(self):
        pass

circle1 = Circle((200, 200, 100),10)
cube1 = Cube((000, 000, 000), 4, 2, 5, 4, 5)
tria1 = Triangle((112,225,225), 25, 25, 25)

print("Цвета")
circle1.set_color(253, 253, 253)
cube1.set_color(254,254,254)
tria1.set_color(255,254,254)
print(circle1.get_color())
print(cube1.get_color())
print(tria1.get_color())

print("Стороны: ")
circle1.set_sides(15)
cube1.set_sides(28, 24, 5, 5, 55, 6, 7, 7, 8, 9, 7, 2)
tria1.set_sides(15, 15, 15)
print(f"Круг{circle1.get_sides()}")
print(f"Куб{cube1.get_sides()}")
print(f"Треугольник{tria1.get_sides()}")

print("Периметр круга")
print(circle1.__len__())

print("Площадь треугольника")
print(tria1.get_square())

print("Объем куба")
print(cube1.get_volume())

print()

