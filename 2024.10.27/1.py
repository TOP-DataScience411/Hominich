from datetime import datetime

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
birthyear = int(input("Введите год рождения "))
year = datetime.now().year - birthyear

print(surname, name, end = ", ")
print(year)
