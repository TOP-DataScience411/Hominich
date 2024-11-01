interval = int(input("Введите интервал в минутах: "))

hours = interval//60
minutes = interval%60

print(f"{interval} мин. это {hours} ч. {minutes} мин.")
#Введите интервал в минутах: 160
#160 мин. это 2 ч. 40 мин.
