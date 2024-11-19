def orth_triangle(cathetus1: float = None, cathetus2: float = None, hypotenuse: float = None):

    arguments = [cathetus1, cathetus2, hypotenuse]
    if all(arg for arg in arguments):
        return None
    if any(arg is not None and arg <= 0 for arg in arguments):
        return None

    if cathetus1 and cathetus2:
        return (cathetus1 ** 2 + cathetus2 ** 2) ** 0.5
    elif hypotenuse and cathetus1 and hypotenuse > cathetus1:
        return (hypotenuse ** 2 - cathetus1 ** 2) ** 0.5
    elif hypotenuse and cathetus2 and hypotenuse > cathetus2:
        return (hypotenuse ** 2 - cathetus2 ** 2) ** 0.5
    else:
        return None

# python3 -i 6.py
# >>> orth_triangle(cathetus1=3, hypotenuse=5)
# 4.0
# >>> orth_triangle(cathetus1=8, cathetus2=15)
# 17.0
# >>> print(orth_triangle(cathetus2=9, hypotenuse=3))
# None
# >>> print(orth_triangle(cathetus2=9))
# None
# >>> print(orth_triangle(cathetus1=3, cathetus2=9, hypotenuse=3))
# None
# >>>
