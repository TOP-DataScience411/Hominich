class ChessKing:
    files = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    ranks = {str(i): i for i in range(1, 9)}

    def __init__(self, color: str = 'white', square: str = None):
        self.color = color.lower()
        if self.color not in ('white', 'black'):
            raise ValueError("Цвет должен быть 'white' или 'black'")
        self.square = square if square else ('e1' if self.color == 'white' else 'e8')

    def __repr__(self):
        return f"{self.color[0].upper()}K: {self.square}"

    def __str__(self):
        return self.__repr__()

    def is_turn_valid(self, new_square: str) -> bool:
        if new_square not in (f + r for f in self.files for r in self.ranks):
            return False

        old_file, old_rank = self.square[0], self.square[1]
        new_file, new_rank = new_square[0], new_square[1]

        file_diff = abs(self.files[new_file] - self.files[old_file])
        rank_diff = abs(self.ranks[new_rank] - self.ranks[old_rank])

        return max(file_diff, rank_diff) == 1

    def turn(self, new_square: str) -> None:
        if self.is_turn_valid(new_square):
            self.square = new_square
        else:
            raise ValueError

# python3 -i 3.py
# >>> wk = ChessKing()
# >>> wk.color
# 'white'
# >>> wk.square
# 'e1'
# >>> wk.turn('e2')
# >>> wk
# WK: e2
# >>> wk.turn('d4')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/margarita/Документы/DataScience411/Hominich/2024.12.15/3.py", line 33, in turn
#     raise ValueError
# ValueError
# >>> bk = ChessKing('black')
# >>> print(bk)
# BK: e8
