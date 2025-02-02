class Tetrahedron:
    def __init__(self, edge: float):
        self.edge = float(edge)

    def surface(self) -> float:
        return (3 ** 0.5) * self.edge ** 2

    def volume(self) -> float:
        return (self.edge ** 3) / (6 * (2 ** 0.5))

# python3 -i 1.py
# >>> t1 = Tetrahedron(5)
# >>> t1.edge
# 5.0
# >>> t1.surface()
# 43.30127018922193
# >>> t1.volume()
# 14.731391274719739
# >>> t1.edge = 6
# >>> t1.surface()
# 62.35382907247958
# >>>
