class Row:
    def __init__(self, **kwargs):
        """Принимаем произвольное число именованных аргументов и устанавливаем их экземпляру"""
        self.__dict__.update(kwargs)
         
    def __setattr__(self, name, value):
        """Запрещаем создание новых и изменение имеющихся атрибутов"""
        if name not in self.__dict__:
            raise AttributeError("Установка нового атрибута невозможна")
        raise AttributeError("Изменение значения атрибута невозможно")
    
    def __delattr__(self, name):
        """Запрещаем удаление атрибутов"""
        raise AttributeError("Удаление атрибута невозможно")
    
    def __repr__(self):
        return f"Row({', '.join(['='.join((key, repr(value))) for key, value in self.__dict__.items()])})"
    
    def __eq__(self, other):
        if isinstance(other, Row):
            return tuple(self.__dict__.items()) == tuple(other.__dict__.items())
        return NotImplemented
    
    def __hash__(self):
        return hash(tuple(self.__dict__.items()))
    
# TEST_1:
row = Row(a='A', b='B', c='C')

print(row)  # Row(a='A', b='B', c='C')
print(row.a, row.b, row.c)  # A B C

# TEST_2:
row1 = Row(a=1, b=2, c=3)
row2 = Row(a=1, b=2, c=3)
row3 = Row(b=2, c=3, a=1)

print(row1 == row2)  # True
print(hash(row1) == hash(row2))  # True
print(row1 == row3)  # False
print(hash(row1) == hash(row3))  # False

# TEST_3:
row = Row(a=1, b=2, c=3)

try:
    row.d = 4
except AttributeError as e:
    print(e)  # Установка нового атрибута невозможна

# TEST_4:
row = Row(a=1, b=2, c=3)

try:
    row.a = 10
except AttributeError as e:
    print(e)  # Изменение значения атрибута невозможно

# TEST_5:
row = Row(a=1, b=2, c=3)

try:
    del row.a
except AttributeError as e:
    print(e)  # Удаление атрибута невозможно

# TEST_6:
row = Row(a=16, b=100, country='Jamaica')
print(row.__eq__(1))  # NotImplemented
print(row.__ne__(1.1))  # NotImplemented