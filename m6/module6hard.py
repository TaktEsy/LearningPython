class Figure:
    SIDES_COUNT = 0
    __sides: int
    __color: list
    filled: bool


    def __init__(self, color, sides):
        self.__sides = sides

        if(self.__is_valid_color(color[0], color[1], color[2])):
            self.set_color(color[0], color[1], color[2])

    # Геттеры
    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    # isВалиды
    def __is_valid_color(self, r, g, b):
        if r not in range(0, 255):
            raise ("Incorrect R")
        elif g not in range(0, 255):
            raise ("Incorrect G")
        elif b not in range(0, 255):
            raise ("Incorrect G")
        else:
            return True

    def __is_valid_sides(self):
        pass

   # Сеттеры
    def set_color(self, r, g, b):
        self.__color.append(r)
        self.__color.append(g)
        self.__color.append(b)
    def set_sides(self, *new_sides):
        pass


    def __len__(self):
        pass

class Circle(Figure):
    SIDES_COUNT = 1



circle1 = Circle((200, 200, 100),10)

print(circle1.get_color())
