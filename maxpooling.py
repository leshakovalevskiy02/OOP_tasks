class MaxPooling:
    """
    В нейронных сетях использую операцию под названием Max Pooling. Суть ее состоит в сканировании прямоугольной таблицы чисел (матрицы)
    окном определенного размера (обычно, 2x2 элемента) и выбора наибольшего значения в пределах этого окна.
    Если окна выходят за пределы матрицы, то они пропускаются (игнорируются)
    """
    def __init__(self, step=(2, 2), size=(2, 2)):
        """
        step - шаг смещения окна по горизонтали и вертикали;
        size - размер окна по горизонтали и вертикали.
        """
        self.step = step
        self.size = size

    @staticmethod
    def __correct_data(matrix):
        """
        Если matrix не является прямоугольной таблицей или содержит хотя бы одно не числовое значение,
        то должно генерироваться исключение командой:
        raise ValueError("Неверный формат для первого параметра matrix.")
        """
        set_ln = set()
        if type(matrix) is not list:
            raise ValueError("Неверный формат для первого параметра matrix.")
        for row in matrix:
            if type(row) is not list:
                raise ValueError("Неверный формат для первого параметра matrix.")
            set_ln.add(len(row))
            for el in row:
                if type(el) not in (int, float):
                    raise ValueError("Неверный формат для первого параметра matrix.")
            if len(set_ln) > 1:
                raise ValueError("Неверный формат для первого параметра matrix.")

    def __calculate_matrix(self, matrix):
        """
        Основная логика выполнения операции MaxPooling
        """
        rows, cols = len(matrix), len(matrix[0])
        i = j = 0
        lst_res = []
        x_shift, y_shift, x_size, y_size = self.step[0], self.step[1], self.size[0], self.size[1]
        while i < rows:
            lst_row = []
            while j < cols:
                mtrx = [matrix[i + ii][j + jj] for ii in range(y_size) for jj in range(x_size) if
                        i + ii < rows and j + jj < cols]
                if len(mtrx) == x_size * y_size:
                    lst_row.append(max(mtrx))
                j += x_shift
            lst_res.append(lst_row)
            j = 0
            i += y_shift
        ln = len(lst_res[0])
        return list(filter(lambda x: len(x) == ln, lst_res))

    def __call__(self, matrix):
        """При вызове экземпляра класса как функции, 
        производится операция MaxPooling"""
        self.__correct_data(matrix)
        return self.__calculate_matrix(matrix)


mp = MaxPooling(step=(2, 2), size=(2, 2))
print(mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]))  # [[6, 8], [9, 7]]
print(mp([[5, 0, 88, 2, 7, 65],
          [1, 33, 7, 45, 0, 1],
          [54, 8, 2, 38, 22, 7],
          [73, 23, 6, 1, 15, 0],
          [4, 12, 9, 1, 76, 6],
          [0, 15, 10, 8, 11, 78]]))  # [[33, 88, 65], [73, 38, 22], [15, 10, 78]]
print(mp([[1, 5, 2], [7, 0, 1], [4, 10, 3]]))  # [[7]]
mp = MaxPooling((4, 2), (1, 2))
print(mp([[71, 39, 31, 92, 60, 15],
          [45, 37, 46, 65, 29, 62],
          [46, 43, 58, 82, 78, 57],
          [88, 43, 40, 82, 43, 49],
          [69, 55, 38, 43, 12, 57],
          [75, 90, 42, 56, 53, 51]]
         ))  # [[71, 60], [88, 78], [75, 53]]
mp = MaxPooling()
print(mp([[1], [1], [1], [1], [1], [1]]))  # [[], [], []]
mp = MaxPooling((4, 5), (1, 3))
print(mp([[71, 39, 31, 92, 60, 15],
          [45, 37, 46, 65, 29, 62],
          [46, 43, 58, 82, 78, 57],
          [88, 43, 40, 82, 43, 49],
          [69, 55, 38, 43, 12, 57],
          [75, 90, 42, 56, 53, 51]]
         ))  # [[71, 78]]
