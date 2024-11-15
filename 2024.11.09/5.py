from ref5 import scores_letters

word = input("Введите слово: ").upper().replace('Ё', 'Е')

one_letter = {letter: score for score, letters in scores_letters.items() for letter in letters}

score = sum(one_letter.get(letter, 0) for letter in word)

print("Количество очков: ", score)

# Введите слово: Пятёрка
# Количество очков:  11
