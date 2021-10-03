class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return " ".join(map(lambda r: '     '.join(map(str, r)), self.matrix))+"\n"

    def __add__(self, other):
        return Matrix(map(lambda r_1, r_2: map(lambda x, y: x + y, r_1, r_2), self.matrix, other.matrix))


my_m1 = Matrix([[31, 22]])
my_m2 = Matrix([[37, 81]])
my_m3 = Matrix([[51, 86]])
print(my_m1)
print(my_m2)
print(my_m3)
s = my_m1 + my_m2 + my_m3
print(s)
my_m1 = Matrix([[3, 5, 32]])
my_m2 = Matrix([[2, 4, 6]])
my_m3 = Matrix([[-1, 64, -8]])
print(my_m1)
print(my_m2)
print(my_m3)
s = my_m1 + my_m2 + my_m3
print(s)
my_m1 = Matrix([[3, 5, 8, 3]])
my_m2 = Matrix([[8, 3, 7, 1]])
print(my_m1)
print(my_m2)
s = my_m1 + my_m2
print(s)
