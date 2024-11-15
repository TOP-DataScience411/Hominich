sequence1 = list(map(int, input("Первая последовательность чисел: ").split()))
sequence2 = list(map(int, input("Вторая последовательность чисел: ").split()))

if len(sequence2) != 0 and len(sequence2) <= len(sequence1):
    if sequence2[0] in sequence1:
        index = sequence1.index(sequence2[0])
        if sequence1[index : index + len(sequence2)] == sequence2:
            print("Да")
        else:
            print("Нет")
elif len(sequence2) == 0:
    print("Да")
else:
    print("Нет")

# Первая последовательность чисел: 1 2 4 6 8
# Вторая последовательность чисел: 4 6
# Да

# Первая последовательность чисел: 2 3 5
# Вторая последовательность чисел: 2 5
# Нет
