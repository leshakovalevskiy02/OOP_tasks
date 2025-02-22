class Matrix:
    def __init__(self, rows, cols, value=0):
        """
        rows - количество строк
        cols - количество столбцов 
        value - значение элементов матрицы (по умолчанию 0)
        """
        self.rows = rows
        self.cols = cols
        self.matrix = [[value] * self.cols for _ in range(self.rows)]
        
    def get_value(self, row, col):
        """Получение значения матрицы по индексу"""
        return self.matrix[row][col]
    
    def set_value(self, row, col, value):
        """Изменение значения матрицы по индексу"""
        self.matrix[row][col] = value
        
    def __repr__(self):
        """Формальное представление"""
        return f"Matrix({self.rows}, {self.cols})"
    
    def __str__(self):
        """Неформальное представление"""
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])
    
    def __pos__(self):
        """Унарный оператор '+' возвращает новый объект матрицы с теми же значениями"""
        matrix = Matrix(self.rows, self.cols)
        matrix.matrix = self.matrix
        return matrix
    
    def __neg__(self):
        """Унарный оператор '-' возвращает новый объект матрицы с инвертированными значениями"""
        matrix = Matrix(self.rows, self.cols)
        matrix.matrix = [[-item for item in row] for row in self.matrix]
        return matrix
    
    def __invert__(self):
        """Унарный оператор '~' возвращает транспорированную матрицу с теми же значениями"""
        matrix = Matrix(self.cols, self.rows)
        matrix.matrix = [list(row) for row in zip(*self.matrix)]
        return matrix
    
    def __round__(self, n=0):
        """Функция round(obj, n=0) возращает новый объект матрицы с округленными до n знаков значениями"""
        matrix = Matrix(self.rows, self.cols)
        matrix.matrix = [[round(item, n) for item in row] for row in self.matrix]
        return matrix 
    

# TEST_1:
matrix = Matrix(2, 3, 1)

print(+matrix)
print()
print(-matrix)
print()
print(~matrix)

# TEST_2:
matrix = Matrix(2, 3)

print(matrix.get_value(0, 0))
print(matrix.get_value(1, 1))

matrix.set_value(0, 0, 100)
matrix.set_value(1, 1, 200)

print(matrix.get_value(0, 0))
print(matrix.get_value(1, 1))


# TEST_3:
matrix1 = Matrix(4, 2)
matrix2 = Matrix(10, 20, value=6)

print(repr(matrix1))
print(repr(matrix2))


# TEST_4:
matrix = Matrix(2, 3, 1)

plus_matrix = +matrix
minus_matrix = -matrix
invert_matrix = ~matrix

print(plus_matrix.cols, plus_matrix.rows)
print(minus_matrix.cols, minus_matrix.rows)
print(invert_matrix.cols, invert_matrix.rows)