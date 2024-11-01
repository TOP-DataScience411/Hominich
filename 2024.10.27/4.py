number = int(input("Введите трехзначное положительное число:"))

first = number//100
second = number//10%10
third = number%10

print(f"Сумма цифр {first+second+third}")
print(f"Произведение цифр {first*second*third}")
