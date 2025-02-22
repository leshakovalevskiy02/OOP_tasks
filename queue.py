from collections import deque

class Queue:
    def __init__(self, *args):
        """
        args - произвольное число элементов очереди.
        В качестве структуры для хранения выбран deque из collections
        """
        self.queue = deque(args)
            
    def __str__(self):
        return " -> ".join(map(str, self.queue))
    
    def add(self, *args):
        """Добавление элементов в очередь"""
        self.queue.extend(args)
        
    def pop(self):
        """Извлечение из начала очереди"""
        if self.queue:
            return self.queue.popleft()
        
    def __eq__(self, other: "Queue"):
        if isinstance(other, Queue):
            return self.queue == other.queue
        return NotImplemented
    
    def __add__(self, other: "Queue"):
        if isinstance(other, Queue):
            return Queue(*self.queue, *other.queue)
        return NotImplemented
        
    def __iadd__(self, other: "Queue"):
        if isinstance(other, Queue):
            self.add(*other.queue)
            return self
        return NotImplemented
    
    def __rshift__(self, n: int):
        """Извлечение n элементов из очереди и вывод оставшихся элементов.
        Реализация через итератор
        """
        if isinstance(n, int):
            it = iter(self.queue)
            for _ in zip(range(n), it):
                pass
            return Queue(*it)
        return NotImplemented
    
# TEST_1:
queue = Queue(1, 2)
queue.add(3)
queue.add(4, 5)

print(queue)
print(queue.pop())
print(queue)

# TEST_2:
queue1 = Queue(1, 2, 3)
queue2 = Queue(1, 2)

print(queue1 == queue2)
queue2.add(3)
print(queue1 == queue2)

# TEST_3:
queue1 = Queue(1, 2, 3)
queue2 = Queue(4, 5)

print(queue1 + queue2)

# TEST_4:
queue1 = Queue(1, 2, 3)
queue2 = Queue(4, 5)

queue1 += queue2

print(queue1)

# TEST_5:
queue = Queue(1, 2, 3, 4, 5)

print(queue >> 3)

# TEST_6:
queue = Queue(1, 2, 3)
print(queue.__add__([]))
print(queue.__iadd__('bee'))
print(queue.__rshift__('geek'))