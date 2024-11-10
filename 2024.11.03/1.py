multiples = []

while True:
    try:
        number = int(input("Введите целое число: "))
    except ValueError:
        print("Похоже, что это не целое число...")
        continue

    if number % 7 == 0:
        multiples.append(number)
    else:
        break

print(" ".join(map(str, multiples[::-1])))

# Введите число: 14
# Введите число: 7
# Введите число: 21
# Введите число: 9
# 21 7 14
