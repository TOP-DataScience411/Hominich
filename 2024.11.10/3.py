def numbers_strip(numbers, n = 1, copy = False):

    changed_numbers = numbers.copy() if copy else numbers

    for _ in range(n):
        changed_numbers.remove(min(changed_numbers))
        changed_numbers.remove(max(changed_numbers))

    return changed_numbers

# python3 -i 3.py
# >>> sample = [4, 8, 1, 9, 7]
# >>> sample_stripped = numbers_strip(sample)
# >>> print(sample_stripped) 
# [4, 8, 7]
# >>> print(sample is sample_stripped) 
# True
# >>> sample = [10, 20, 30, 40, 50, 60, 70, 80]
# >>> sample_stripped = numbers_strip(sample, 3, copy=True)
# >>> print(sample_stripped) 
# [40, 50]
# >>> print(sample is sample_stripped)
# False
# >>> 
