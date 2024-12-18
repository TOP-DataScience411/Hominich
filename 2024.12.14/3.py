from pathlib import Path
import importlib.util
from utils import load_file

def ask_for_file():
    """
    Функция запрашивает у пользователя путь к потерянному файлу и копирует этот файл с помощью функции load_file.
    """
    while True:
        file_path = input("путь: ").strip()
        path = Path(file_path)

        if not path.is_file():
            print("! по указанному пути отсутствует необходимый файл !")
        else:
            break

    copied_file = load_file(path)

    spec = importlib.util.spec_from_file_location("conf.py", copied_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module

# python3 -i 3.py
# >>> config_module = ask_for_file()
# путь: /home/margarita/Документы/DataScience411/Hominich/2024.12.14/conf.py
# ! по указанному пути отсутствует необходимый файл !
# путь: /home/margarita/Документы/DataScience411/Hominich/2024.12.14/data/conf.py
# >>> config_module.defaults
# {'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}
# >>>
