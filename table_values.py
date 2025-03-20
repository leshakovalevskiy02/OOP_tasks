class IntegerValue:
    """Дескриптор, проверяющий, что переданное значение типа int"""
    def __set_name__(self, owner, name):
        self.name = f"_{name}"
        
    def __set__(self, instance, value):
        if type(value) is not int:
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)
    
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    

class StringValue:
    """Дескриптор, проверяющий, что переданное значение типа str"""
    def __set_name__(self, owner, name):
        self.name = f"_{name}"
        
    def __set__(self, instance, value):
        if type(value) is not str:
            raise ValueError('возможны только строковые значения')
        setattr(instance, self.name, value)
    
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
   
class Cell:
    """Родительский класс для ячеек Cell"""
    _START_VALUE = None
    
    def __init__(self, start_value=None):
        self.value = start_value or self._START_VALUE
    
class CellInteger(Cell):
    """Класс для ячеек Cell типа int"""
    value = IntegerValue()
    _START_VALUE = 0
        
        
class CellString(Cell):
    """Класс для ячеек Cell типа str"""
    value = StringValue()
    _START_VALUE = ""

        
class TableValues:
    def __init__(self, rows, cols, cell=None):
        """Класс реализующий таблицу, где при обращении по индексу(кортежу) срабатывают методы getitem, setitem
        Вызов obj[1, 1] => obj[1][1]
        """
        if cell is None:
            raise ValueError('параметр cell не указан')
        self.rows = rows
        self.cols = cols
        self.cells = tuple(tuple(cell() for j in range(cols)) for i in range(rows))
        
    def __correct_index(self, ind, size):
        if type(ind) is not int or ind < 0 or ind >= size:
            raise IndexError("Неверный индекс")
        
    def __getitem__(self, item):
        i, j = item
        self.__correct_index(i, self.rows)
        self.__correct_index(j, self.cols)
        return self.cells[i][j].value
    
    def __setitem__(self, key, value):
        i, j = key
        self.__correct_index(i, self.rows)
        self.__correct_index(j, self.cols)
        self.cells[i][j].value = value
        

table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
try:
    table[0, 0] = 1.45 # генерируется исключение ValueError
except ValueError as v:
    print(v)

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()
    
table2 = TableValues(2, 3, cell=CellString)
print(table2[0, 1])
table2[1, 2] = "w"
try:
    table2[0, 0] = 1 # генерируется исключение ValueError
except ValueError as v:
    print(v)

for row in table2.cells:
    for x in row:
        print(x.value, end=' ')
    print()