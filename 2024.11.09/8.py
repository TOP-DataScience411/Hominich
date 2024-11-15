files = input("Введите последовательность имен файлов, разделённых точкой с запятой и символом пробела: ").split("; ")

count = {}
renamed_files = []

for name in files:
    if name not in count:
        count[name] = 1
        renamed_files.append(name)
    else:
        count[name] += 1
        dot_index = name.find('.')
        if dot_index != -1:
            new_name = f"{name[:dot_index]}_{count[name]}{name[dot_index:]}"
            renamed_files.append(new_name)
        else:
            renamed_files.append(name)

renamed_files.sort()

for name in renamed_files:
    print(name)

# Введите последовательность имен файлов, разделённых точкой с запятой и символом пробела: 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz
# 1.py
# 1_2.py
# 1_3.py
# aux.h
# functions.h
# main.cpp
# main_2.cpp
# main_3.cpp
# src.tar.gz
# src_2.tar.gz
