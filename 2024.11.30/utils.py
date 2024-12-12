from shutil import get_terminal_size

def important_message(message: str) -> str:
    """
    Функция important_message принимает обязательным позиционно-ключевым аргументом текст сообщения в виде объекта str.
    Функция important_message возвращает объект str.
    
    Задача этой функции — сгенерировать строку, в которой переданный текст будет обрамлён рамкой из символов '=' и '#'.
        Ширина рамки определяется текущей шириной окна терминала.
        Пустое пространство внутри рамки заполняется пробелами.
        Между верхней границей рамки и первой строчкой текста должен быть отступ одна строчка.
        Между последней строчкой текста и нижней границей рамки должен быть отступ одна строчка.
        Текст внутри рамки выравнивается по центру.
        Между боковыми границами рамки и текстом должен быть минимальный отступ два пробела.
    """
    terminal_width = get_terminal_size().columns - 1
    border = "#" + "=" * (terminal_width - 2) + "#"
    empty_line = "#" + " " * (terminal_width - 2) + "#"

    max_text_width = terminal_width - 6
    words = message.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= max_text_width:
            current_line += " " + word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    text_lines = ["#  " + line.center(max_text_width) + "  #" for line in lines]

    result = [border, empty_line] + text_lines + [empty_line, border]
    return "\n".join(result)
