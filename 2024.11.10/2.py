def taxi_cost(distance: int, waiting: int = 0) -> int | None:

    basic_cost = 80

    if distance < 0 or waiting < 0:
        return None
    elif distance == 0:
        basic_cost += 80 + waiting * 3
    else:
        basic_cost += (distance / 150) * 6
        basic_cost += waiting * 3

    return round(basic_cost)

# python3 -i 2.py
# >>> taxi_cost(500)
# 100
# >>> taxi_cost(0, 3)
# 169
# >>> print(taxi_cost(-300))
# None
# >>> 
