fruits = []
while True:
    fruit = input("Введите название фрукта: ")
    if fruit != "":
        fruits.append(fruit)
    else:
         break

if fruits:
    result = " и ".join([", ".join(fruits[:-1]), fruits[-1]]) if len(fruits) > 1 else fruits[0]
    print(result)

# Введите название фрукта: манго
# Введите название фрукта: апельсин
# Введите название фрукта:
# манго и апельсин

# Введите название фрукта: манго
# Введите название фрукта: апельсин
# Введите название фрукта: лимон
# Введите название фрукта:
# манго, апельсин и лимон
