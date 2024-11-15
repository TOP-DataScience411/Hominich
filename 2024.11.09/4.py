dictionary = {}

while True:
    try:
        element = input("Вводим элементы для словаря: ")
        if not element
            break
        key, value = element.split(maxsplit = 1)
        dictionary[value] = key
    except ValueError:
        continue

search_value = input("Что найти в словаре? ")

try:
    print(dictionary[search_value])
except KeyError:
    print("! value error !")

# Вводим элементы для словаря: asa утро
# Вводим элементы для словаря: hiru день
# Вводим элементы для словаря: yoru ночь
# Вводим элементы для словаря:
# Что найти в словаре? день
# hiru
