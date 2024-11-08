def find_color(cell):
    if len(cell) == 2:
        horizontal = ["a", "b", "c", "d", "e", "f", "g", "h"]
        verticalInt = list(range(1, 9))
        vertical = list(map(str, verticalInt))

        oddH = horizontal[0 : : 2]
        evenH = horizontal[1 : : 2]
        oddV = vertical[0 : : 2]
        evenV = vertical[1 : : 2]

        if (cell[0] in oddH and cell[1] in oddV) or (cell[0] in evenH and cell[1] in evenV):
            color = "Black"
            return color
        elif (cell[0] in oddH and cell[1] in evenV) or (cell[0] in evenH and cell[1] in oddV):
            color = "White"
            return color
        else:
            print("Присутствуют неизвестные элементы")
    else:
        print("Произошел некорректный ввод")

cell1 = input("Введите координаты первой клетки: ")
cell2 = input("Введите координаты второй клетки: ")

color1 = find_color(cell1)
color2 = find_color(cell2)

if color1 == color2 and color1 and color2:
    print("Да")
elif color1 != color2 and color1 and color2:
    print("Нет")
else:
    print("Произошел некорректный ввод")

# Введите координаты первой клетки: c5
# Введите координаты второй клетки: d1
# Нет
