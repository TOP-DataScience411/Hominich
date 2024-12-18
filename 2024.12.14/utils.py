from pathlib import Path
from shutil import copy2

def load_file(file_path: Path) -> Path:
    """
    Функция осуществляет копирование файла по переданному пути в основной каталог (каталог задания).
    """
    destination = Path.cwd() / file_path.name
    copy2(file_path, destination)
    return destination
