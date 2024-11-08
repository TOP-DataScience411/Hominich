number = []
for i in range(2):
    try:
        num = int(input(f"Введите {i+1} целое число: "))
    except ValueError:
        print("Похоже, что это не целое число...")
        num = int(input(f"Введите {i+1} целое число: "))
    finally:
        number.append(num)

if number[1] != 0:
    if number[0] % number[1] == 0:
        quotient = number[0] // number[1]
        print(f"{number[0]} делится на {number[1]} нацело", f"частное: {quotient}", sep = "\n")
    else:
        quotient = number[0] // number[1]
        remainder = number[0] % number[1]
        print(f"{number[0]} не делится на {number[1]} нацело", f"неполное частное: {quotient}", f"остаток: {remainder}", sep = "\n")
else:
    print("Деление на ноль!")

# Введите 1 целое число: t
# Похоже, что это не целое число...
# Введите 1 целое число: 7
# Введите 2 целое число: 2
# 7 не делится на 2 нацело
# неполное частное: 3
# остаток: 1
