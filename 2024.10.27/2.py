number = int(input("Введите целое число: "))

prev = f"Перед числом {number} находится число {number-1}."
# ПЕРЕИМЕНОВАТЬ: next — это имя встроенной функции, объявляя собственную переменную с таким именем вы теряете прямой доступ к встроенной функции
next = f"После числа {number} идет число {number+1}."

# ИСПРАВИТЬ: вывод не соответствует требуемому формату (неверный текст, лишние символы)
print(prev, next, sep = "\n")
# КОММЕНТАРИЙ: в случае, если вы будете генерировать строку не для чтения человеком, а для другой функции/класса/программы — неверный формат может стоить вам неработающего приложения


#Введите целое число: 33
#Перед числом 33 находится число 32.
#После числа 33 идет число 34.


# ИТОГ: доработать — 2/3

