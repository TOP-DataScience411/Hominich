cell1 = input("Введите координаты первой клетки: ")
cell2 = input("Введите координаты второй клетки: ")

horizontal = ["a", "b", "c", "d", "e", "f", "g", "h"]
verticalInt = list(range(1, 9))
vertical = list(map(str, verticalInt))

if (
        len(cell1) == 2
    and len(cell2) == 2
    and cell1[0] in horizontal
    and cell2[0] in horizontal
    and cell1[1] in vertical
    and cell2[1] in vertical
):
    if cell1[0] == cell2[0] or cell1[1] == cell2[1]:
        print("Да")
    else:
        print("Нет")
else:
    print("Произошел некорректный ввод")

# Введите координаты первой клетки: b3
# Введите координаты второй клетки: b7
# Да
