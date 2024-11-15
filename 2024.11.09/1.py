email = input("Введите e-mail: ")

print("Да" if "@" in email and '.' in email[email.index("@")+1:] else "Нет")

# Введите e-mail: neko.@mailnet
# Нет

# Введите e-mail: neko@mail.da
# Да
