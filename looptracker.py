from copy import copy

class LoopTracker:
    def __init__(self, iterable):
        """
        self._accesses - количество вызовов итератора
        self._empty_accesses - количество вызовов пустого итератора
        self._first - ссылка на первый элемент
        self._last - ссылка на текущий последний элемент
        """
        self.iterator = iter(iterable)
        self._accesses = 0
        self._empty_accesses = 0
        self._first = None
        self._last = None
        
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            next_obj = next(self.iterator)
            self._accesses += 1
            if self._first is None:
                self._first = next_obj
            self._last = next_obj
            return next_obj
        except:
            self._empty_accesses += 1
            raise
    
    def is_empty(self):
        """Проверяем есть ли элементы в итераторе"""
        new_iter = copy(self.iterator)
        try:
            next(new_iter)
            return False
        except StopIteration:
            return True        
    
    @property
    def accesses(self):
        return self._accesses
    
    @property
    def empty_accesses(self):
        return self._empty_accesses
    
    @property
    def first(self):
        """Получение первого элемента итератора, или ошибка AttributeError, если его нет"""
        if self._first is None:
            new_it = copy(self.iterator)
            try:
                return next(new_it)
            except StopIteration:
                raise AttributeError("Исходный итерируемый объект пуст")
        return self._first
    
    @property    
    def last(self):
        """Получение текущего последнего элемента итератора или ошибка AttributeError,
        если итератор не генирировал значений"""
        if self._last is None:
            raise AttributeError("Последнего элемента нет")
        return self._last

# TEST_1:
loop_tracker = LoopTracker([1, 2, 3])

print(loop_tracker.accesses)  # 0
next(loop_tracker)
next(loop_tracker)
print(loop_tracker.accesses)  # 2

# TEST_3:
loop_tracker = LoopTracker([1, 2, 3])
print(loop_tracker.first)  # 1

print(next(loop_tracker))  # 1
print(next(loop_tracker))  # 2
print(loop_tracker.first)  # 1
print(next(loop_tracker))  # 3
print(loop_tracker.first)  # 1

# TEST_3:
loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))  # 1
print(loop_tracker.last)   # 1

print(next(loop_tracker))  # 2
print(loop_tracker.last)   # 2

print(next(loop_tracker))  # 3
print(loop_tracker.last)   # 3

# TEST_3:
loop_tracker = LoopTracker([1, 2])

print(loop_tracker.empty_accesses)  # 0
next(loop_tracker)
next(loop_tracker)

for _ in range(5):
    try:
        next(loop_tracker)
    except StopIteration:
        pass
        
print(loop_tracker.empty_accesses)  # 5

# TEST_4:
loop_tracker = LoopTracker([1, 2])

print(loop_tracker.is_empty())  # False
next(loop_tracker)
print(loop_tracker.is_empty())  # False
next(loop_tracker)
print(loop_tracker.is_empty())  # True

# TEST_5:
loop_tracker = LoopTracker([])

try:
    print(loop_tracker.first)
except AttributeError as e:
    print(e)  # Исходный итерируемый объект пуст

# TEST_6:
loop_tracker = LoopTracker([1, 2, 3])

try:
    print(loop_tracker.last)
except AttributeError as e:
    print(e)  # Последнего элемента нет