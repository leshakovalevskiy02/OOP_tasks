from copy import copy, deepcopy

class Atomic:
    """
    Менеджер контекста - если все операции истинны происходит изменение,
    иначе изменения не принимаются.
    Параметр deep - определяет состояние вложенных структур
    """
    def __init__(self, data, deep=False):
        """
        data - произвольный список, множество или словарь
        deep - булево значение по умолчанию False.
        """
        self.data = data
        self.deep = deep
        
    def __enter__(self):
        if self.deep:
            self.data_copy = deepcopy(self.data)
        else:
            self.data_copy = copy(self.data)
        return self.data
    
    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type is not None:
            self.data.clear()
            if type(self.data_copy) in (dict, set):
                self.data.update(self.data_copy)
            if type(self.data_copy) == list:
                self.data.extend(self.data_copy)
        return True

# TEST_1:
numbers = [1, 2, 3, 4, 5]

with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[1]

print(numbers)

# TEST_2:
numbers = [1, 2, 3, 4, 5]

with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[100]           # обращение по несуществующему индексу

print(numbers)

# TEST_3:
matrix = [[1, 2], [3, 4]]

with Atomic(matrix) as atomic:
    atomic[1].append(0)       # изменение вложенной структуры
    atomic.append([5, 6])
    del atomic[100]           # обращение по несуществующему индексу

print(matrix)

# TEST_4:
matrix = [[1, 2], [3, 4]]

with Atomic(matrix, True) as atomic:
    atomic[1].append(0)       # изменение вложенной структуры
    atomic.append([5, 6])
    del atomic[100]           # обращение по несуществующему индексу

print(matrix)

# TEST_5:
numbers = {1, 2, 3, 4, 5}

with Atomic(numbers) as atomic:
    atomic.add(6)
    atomic.append(7)           # добавление элемента с помощью несуществующего метода

print(sorted(numbers))

with Atomic(numbers) as atomic:
    atomic.add(6)

print(sorted(numbers))

# TEST_6:
data = {'firstname': 'Alyson', 'lastname': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}

with Atomic(data, True) as atomic:          # deep = True
    atomic['birthday']['month'] = 'April'   # изменение вложенной структуры
    print(atomic['name'])                   # обращение по несуществующему ключу

print(data)

with Atomic(data) as atomic:                # deep = False
    atomic['birthday']['month'] = 'April'   # изменение вложенной структуры
    print(atomic['name'])                   # обращение по несуществующему ключу

print(data)

# TEST_7:
data = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}

with Atomic(data) as atomic:
    atomic['e'] += 2   # изменение структуры

print(data)

# TEST_8:
matrix = [[1, 2], [3, 4]]

with Atomic(matrix, True) as atomic:
    atomic[1].append(0)

print(matrix)