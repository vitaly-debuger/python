class Matrix:
    def __init__(self, my_list):
        self.ml = my_list

    def __str__(self):
        return '\n'.join(['\t'.join([str(j) for j in i]) for i in self.ml])

    def __add__(self, other):
        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.ml)):

            for j in range(len(self.ml[0])):
                result[i][j] = self.ml[i][j] + other.ml[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in result]))



matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 0]])
print(f"{matrix_1}\n")
print(matrix_1 + matrix_2)