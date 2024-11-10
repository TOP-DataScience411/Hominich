def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

while True:
    try:
        n = int(input("Введите количество разрядов: "))
        0 / n
        break
    except ValueError:
        continue
    except ZeroDivisionError:
        continue

min = int("1" + "0" * (n - 1))
max = int("9" * n)

prime_count = 0

for number in range(min, max + 1):
    if is_prime(number):
        prime_count += 1

print(f"Количество простых чисел среди всех {n}-значных чисел:", prime_count)

# Введите количество разрядов: 4
# Количество простых чисел среди всех 4-значных чисел: 1061
