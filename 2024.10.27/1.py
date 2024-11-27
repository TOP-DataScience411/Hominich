from datetime import datetime

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
birthyear = int(input("Введите год рождения "))
year = datetime.now().year - birthyear

print(surname, name+",", year)


#Введите имя: Рита
#Введите фамилию: Хоминич
#Введите год рождения 1990
#Хоминич Рита, 34


# ИТОГ: отлично — 4/4

