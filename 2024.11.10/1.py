def strong_password(password):
    if len(password) < 8:
        return False

    upper_char = any(char.isupper() for char in password)
    lower_char = any(char.islower() for char in password)
    if not (upper_char and lower_char):
        return False

    digit_count = sum(char.isdigit() for char in password)
    if digit_count < 2:
        return False

    zero_others_char = all(char.isalnum() for char in password)
    if zero_others_char:
        return False

    return True

# python3 -i 1.py
# >>> strong_password('strong_password')
# False
# >>> strong_password('12strong_Password?')
# True
# >>>
