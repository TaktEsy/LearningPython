def draw_area():
    for i in area:
        print(*i)
    print()

area = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
print("Hello!")
draw_area()
row = int(input("Номер строки (1,2,3):")) - 1
col = int(input("Номер столбца (1,2,3):")) - 1
area[row][col] = "X"
draw_area()
