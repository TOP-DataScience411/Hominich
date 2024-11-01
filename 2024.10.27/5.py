integ = input("Введите целую часть числа миль:")
fract = input("Введите дробную часть числа миль:")

milya = float(f"{integ}.{fract}")
km = milya*1.61 #1 миля = 1.61 км

print(f"{milya} миль = {km:.1f} км")
