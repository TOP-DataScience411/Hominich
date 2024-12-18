from pathlib import Path

def list_files(directory: str):
    """
    Возвращает возвращает кортеж с именами файлов в каталоге по переданному пути.
    В случае, если по переданному пути отсутствует каталог, функция возвращает None.
    """
    dir_path = Path(directory)
    if not dir_path.is_dir():
        return None
    files = [file.name for file in dir_path.iterdir() if file.is_file()]
    return tuple(files)

# python3 -i 1.py
# >>> list_files(r'/home/margarita/Документы/DataScience411/Hominich/2024.12.14/data')
# ('E3ln1.txt', 'vars.py', 'questions.quiz', 'le1UO.txt', 'xcD1a.zip', 'conf.py', 'F1jws.jpg', 'q40Kv.docx', '7MD9i.chm', 'r62Bf.txt')
