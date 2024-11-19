from math import prod

def central_tendency(number1: float, number2: float, *numbers: float):

    list_numbers = [number1, number2] + list(numbers)
    n = len(list_numbers)
    dictionary = {}

    sorted_numbers = sorted(list_numbers, reverse=True)
    if n % 2 == 1:
        dictionary['median'] = float(sorted_numbers[n // 2])
    else:
        dictionary['median'] = (sorted_numbers[(n - 1)// 2] + sorted_numbers[(n - 1)// 2 + 1]) / 2

    dictionary['arithmetic']= sum(list_numbers) / n

    dictionary['geometric'] = prod(list_numbers) ** (1 / n)

    dictionary['harmonic'] = n / sum(1 / number for number in list_numbers)

    return dictionary

# python3 -i 5.py
# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.92}
# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}
# >>> 
