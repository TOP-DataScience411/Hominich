positive_sum  = 0

for _ in range(3):
    try:
        number = float(input("Введите число: "))
        if number > 0:
            positive_sum += number
    except ValueError:
        print("Похоже, что это не число...")

if positive_sum.is_integer():
    print("Сумма только положительных чисел:", int(positive_sum))
else:
    print("Сумма только положительных чисел:", positive_sum)

# Введите число: 21
# Введите число: -1.09
# Введите число: 5
# Сумма только положительных чисел: 26
