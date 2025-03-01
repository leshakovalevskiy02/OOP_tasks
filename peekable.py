from copy import copy

OBJECT = object()

class Peekable:
    def __init__(self, iterable):
        """Создаем на основе итерируемого объекта - итератор"""
        self.iterator = iter(iterable)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self.iterator)
    
    def peek(self, default=OBJECT):
        """Метод возвращающий следующий элемент, если он есть, не сдвигая при этом итератор
        Если элементов нет то - StopIteration или значение default"""
        new_it = copy(self.iterator)
        try:
            return next(new_it)
        except StopIteration:
            if default is OBJECT:
                raise
            return default
        
# TEST_1:
iterator = Peekable('Python')

print(next(iterator))
print(iterator.peek())
print(iterator.peek())
print(next(iterator))
print(iterator.peek())
print(iterator.peek())

# TEST_2:
iterator = Peekable(iter([]))

try:
    iterator.peek()
except StopIteration:
    print('Пустой итератор')

try:
    next(iterator)
except StopIteration:
    print('Пустой итератор')

# TEST_3:
iterator = Peekable([n ** 2 for n in [1, 2, 3]])

print(iterator.peek(default=0))
print(*iterator)
print(iterator.peek(default=None))
print(iterator.peek(default=1))
print(iterator.peek(default=[]))
print(iterator.peek(default=()))