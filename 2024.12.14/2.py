import random
import datetime
from typing import Literal

data_directory = "/home/margarita/Документы/DataScience411/Hominich/2024.12.14/data/names"
names = {
    "male": {"names": [], "patronymics": [], "surnames": []},
    "female": {"names": [], "patronymics": [], "surnames": []},
}

def load_names(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []

def load_data() -> None:
    """
    Функция читает из файлов данные и упорядочивает их.
    """
    global names

    male_data = load_names(f"{data_directory}/мужские_имена_отчества.txt")
    for entry in male_data:
        base_name, variants = entry.split(" (")
        variants = variants.rstrip(")").split(", ")
        names["male"]["names"].append(base_name)
        names["male"]["patronymics"].append(variants[0])
        names["female"]["patronymics"].append(variants[1])

    female_names = load_names(f"{data_directory}/женские_имена.txt")
    names["female"]["names"] = female_names

    last_names = load_names(f"{data_directory}/фамилии.txt")
    for last_name in last_names:
        if "," in last_name:
            male, female = map(str.strip, last_name.split(","))
            names["male"]["surnames"].append(male)
            names["female"]["surnames"].append(female)
        else:
            names["male"]["surnames"].append(last_name)
            names["female"]["surnames"].append(last_name)

def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def random_birth_date(start_year: int, end_year: int) -> datetime.date:
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)

    if month in {1, 3, 5, 7, 8, 10, 12}:
        day = random.randint(1, 31)
    elif month in {4, 6, 9, 11}:
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 29 if is_leap_year(year) else 28)

    return datetime.date(year, month, day)

def generate_person() -> dict:
    """
    Функция генерирует анкету человека со случайными данными.
    """
    gender: Literal['мужской', 'женский'] = random.choice(["мужской", "женский"])
    gender_key = "male" if gender == "мужской" else "female"

    name = random.choice(names[gender_key]["names"])
    patronymic = random.choice(names[gender_key]["patronymics"])
    surname = random.choice(names[gender_key]["surnames"])

    birth_date = random_birth_date(1925, 2024)

    phone_number = f"+79{random.randint(100000000, 999999999)}"

    return {
        "имя": name,
        "отчество": patronymic,
        "фамилия": surname,
        "пол": gender,
        "дата рождения": birth_date,
        "мобильный": phone_number,
    }

# python3 -i 2.py
# >>> from pprint import pprint
# >>> load_data()
# >>> pprint(generate_person(), sort_dicts=False)
# {'имя': 'Флавия',
#  'отчество': 'Аркадиевна',
#  'фамилия': 'Поленова',
#  'пол': 'женский',
#  'дата рождения': datetime.date(1971, 3, 10),
#  'мобильный': '+79239183862'}
# >>> pprint(generate_person(), sort_dicts=False)
# {'имя': 'Арефий',
#  'отчество': 'Меркулович',
#  'фамилия': 'Фонвизин',
#  'пол': 'мужской',
#  'дата рождения': datetime.date(1934, 3, 28),
#  'мобильный': '+79824039603'}
# >>> 
