while True:
    try:
        n = int(input("Введите количество чисел последовательности Фибоначчи: "))
        break
    except ValueError:
        continue

if n > 0:
    fib = [1]
    if n > 1:
        fib.append(1)
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])

print(*fib)

# Введите количество чисел последовательности Фибоначчи: 15
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610
