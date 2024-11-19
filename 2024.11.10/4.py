def countable_nouns(number: int, noun_forms: tuple[str, str, str]) -> str:

    if 10 <= number % 100 <= 19:
        return noun_forms[2]
    elif number % 10 == 1:
        return noun_forms[0]
    elif 2 <= number % 10 <= 4:
        return noun_forms[1]
    else:
        return noun_forms[2]

# python3 -i 4.py
# >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(19, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(33, ("год", "года", "лет"))
# 'года'
# >>> 
