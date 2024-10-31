interval = int(input("Введите интервал в минутах: "))

hours = interval//60
minutes = interval%60

print(f"{interval} мин. это {hours} ч. {minutes} мин.")
