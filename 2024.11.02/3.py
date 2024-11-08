try:
    year = int(input("Введите год: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("да")
    else:
        print("нет")
except ValueError:
    print("Возможно это не год")

# Введите год: 2024
# да
