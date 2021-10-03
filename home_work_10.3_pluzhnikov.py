class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['⚽' * rows for _ in range(self.nums // rows)]) + "\n" + '⚽' * (self.nums % rows)

    def __str__(self):
        return f"{self.nums}"

    def __add__(self, other):
        print("Сумма двух ячеек: ")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print("Разность двух ячеек: ")
        return Cell(self.nums - other.nums) if self.nums - other.nums >= 0 \
            else "Колличество ячеек в первой клетке меньше второй, вычитание невозможно!"

    def __mul__(self, other):
        print("Произведение двух ячеек: ")
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print("Деление двух ячеек: ")
        return Cell(self.nums // other.nums)


cell_1 = Cell(int(input("Введите колличество ячеек первых клеток: ")))
cell_2 = Cell(int(input("Введите колличество ячеек вторых клеток: ")))
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(int(input("Введите колличество рядов ячеек: "))))