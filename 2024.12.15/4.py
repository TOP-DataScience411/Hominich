import csv
import pathlib

class CountableNouns:
    db_path = pathlib.Path("words.csv")
    words = {}

    if db_path.exists():
        with db_path.open(encoding="utf-8") as file:
            reader = csv.reader(file)
            words = {row[0]: (row[1], row[2]) for row in reader}

    @classmethod
    def pick(cls, number: int, word: str) -> str:
        if word not in cls.words:
            print(f'существительное "{word}" отсутствует в базе')
            cls.save_words(word)

        if 10 < number % 100 < 20:
            return cls.words[word][1]
        elif number % 10 == 1:
            return word
        elif 2 <= number % 10 <= 4:
            return cls.words[word][0]
        else:
            return cls.words[word][1]

    @classmethod
    def save_words(cls, word1: str = None) -> None:
        new_words = []

        if word1:
            word2 = input(' введите слово, согласующееся с числительным "два": ').strip()
            word5 = input(' введите слово, согласующееся с числительным "пять": ').strip()
            cls.words[word1] = (word2, word5)
            new_words.append((word1, word2, word5))
        else:
            word1 = input(' введите слово, согласующееся с числительным "один": ').strip()
            word2 = input(' введите слово, согласующееся с числительным "два": ').strip()
            word5 = input(' введите слово, согласующееся с числительным "пять": ').strip()
            cls.words[word1] = (word2, word5)
            new_words.append((word1, word2, word5))

        with cls.db_path.open("a", encoding="utf-8", newline="\n") as file:
            writer = csv.writer(file)
            writer.writerows(new_words)

# python3 -i 4.py
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней')}
# >>> CountableNouns.pick(22, 'год')
# 'года'
# >>> CountableNouns.pick(365, 'день')
# 'дней'
# >>> CountableNouns.pick(21, 'попугай')
# существительное "попугай" отсутствует в базе
#  введите слово, согласующееся с числительным "два": попугая
#  введите слово, согласующееся с числительным "пять": попугаев
# 'попугай'
# >>> CountableNouns.pick(22, 'попугай')
# 'попугая'
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'попугай': ('попугая', 'попугаев')}
# >>> CountableNouns.save_words()
#  введите слово, согласующееся с числительным "один": капля
#  введите слово, согласующееся с числительным "два": капли
#  введите слово, согласующееся с числительным "пять": капель
# >>> print(CountableNouns.db_path.read_text(encoding='utf-8'))
# год,года,лет
# месяц,месяца,месяцев
# день,дня,дней
# попугай,попугая,попугаев
# капля,капли,капель
#
# >>>
