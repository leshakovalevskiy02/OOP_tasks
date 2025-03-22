# yield
class Cell:
    def __init__(self, data=0):
        self.__data = data
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, new_data):
        self.__data = new_data
        
        
class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self._table = [[Cell() for j in range(cols)] for i in range(rows)]
        
    def __correct_indx(self, item):
        if len(item) != 2:
            raise IndexError('неверный индекс')
        row, col = item
        if type(row) is not int or row < 0 or row >= self.rows:
            raise IndexError('неверный индекс')
        if type(col) is not int or col < 0 or col >= self.cols:
            raise IndexError('неверный индекс')
        return row, col
        
    def __getitem__(self, item):
        """
        Обращение по индексу: value = table[1, 1]
        """
        i, j = self.__correct_indx(item)
        return self._table[i][j].data
    
    def __setitem__(self, key, value):
        """
        Запись нового значения в ячейку: table[3, 2] = 5
        """
        i, j = self.__correct_indx(key)
        if self.type_data != type(value):
            raise TypeError('неверный тип присваиваемых данных')
        self._table[i][j].data = value
    
    def __iter__(self):
        """
        Метод iter реализовывает функцию генератор, которая,
        в свою очередь, возвращает на каждой итерации выражение-генератор
        """
        for row in self._table:
            yield (el.data for el in row)
    

table = TableValues(4, 4)    
table[1, 1] = 3 # запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
table[3, 2] = 5 # запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
value = table[1, 1] # считывание значения из ячейки с индексами row, col
print(value)

for row in table:  # перебор по строкам
    for value in row: # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()