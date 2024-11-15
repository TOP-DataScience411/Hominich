str = input("Введите двоичное число: ")

if str.startswith('0b'):
    str = str[2:]
elif str.startswith('b'):
    str = str[1:]

print("Да") if set(str) <= {'0', '1'} else print("Нет")

# Введите строку: 01011
# Да

# Введите строку: 0b0210
# Нет
