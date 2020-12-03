class Cell:
    def __init__(self, cell):
        self.cell = int(cell)

    def __str__(self):
        return f"{self.cell}"

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if self.cell > other.cell:
            return Cell(self.cell - other.cell)
        else:
            return f"Разность количества ячеек двух клеток больше нуля"

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        try:
            if other.cell < self.cell:
                return Cell(self.cell / other.cell)
            else:
                return f"Вторая клетка меньше первой"
        except ZeroDivisionError:
            return f"На ноль делить нельзя, или вторая клетка больше первой"

    def make_order(self, raw):
        return (('*' * raw + '\n') * (self.cell // raw) + ('*' *(self.cell % raw) + '\n'))



cell_1 = Cell(12)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print()
print(cell_1.make_order(5))