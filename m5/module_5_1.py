class House:
    def __init__(self, name, number_of_floors ):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print("Too high!")
        elif new_floor == self.number_of_floors:
            print("Already there!")




h1 = House('ЖК Ромашка', 18)
h1.go_to(51)