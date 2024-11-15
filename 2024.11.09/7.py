from ref7 import list_of_dicts

new_dictionary = {}

for dictionary in list_of_dicts:
    for key, value in dictionary.items():
        new_dictionary.setdefault(key, set()).add(value)

for key, values in new_dictionary.items():
    print(f"{key}: {values}")

# Владивосток: {5}
# Воронеж: {1, 4}
# Екатеринбург: {1, 3, 5}
# Иркутск: {9, 2, 5}
# Москва: {3, 4, 6}
# Новокузнецк: {2, 4}
# Оренбург: {1}
# Саратов: {2}
# Уфа: {9}
# Ярославль: {8, 7}
# Волгоград: {5}
# Нижний Новгород: {8, 2, 5}
# Ростов-на-Дону: {6}
# Тольятти: {1}
# Тюмень: {3}
# Казань: {4}
# Новосибирск: {7}
# Пермь: {3}
# Челябинск: {3}
# Санкт-Петербург: {7}
