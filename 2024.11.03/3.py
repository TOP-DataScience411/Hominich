while True:
    try:
        n = int(input("Введите натуральное число: "))
        0 / n
        break
    except ValueError:
        continue
    except ZeroDivisionError:
        continue

sum_of_divisors = 0

for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        sum_of_divisors += i
        if i != n // i:
            sum_of_divisors += n // i

print("Сумма всех делителей числа", sum_of_divisors)

# Введите натуральное число: 51
# Сумма всех делителей числа 72
