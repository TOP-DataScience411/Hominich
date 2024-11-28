def product(numbers) -> float:
    if len(numbers) == 1:
        return float(numbers[0])
    result = float(numbers[0] * product(numbers[1:]))
    return 0.0 if result == -0.0 else result

# >>> product(range(10, 60, 10))
# 12000000.0
# >>> product((0.12, 0.05, -0.09, 0.0, 0.21))
# 0.0
