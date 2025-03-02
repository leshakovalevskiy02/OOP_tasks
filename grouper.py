class Grouper:
    def __init__(self, iterable, key):
        """
        self.group - хранит в качестве ключа название группы(функция key, примененная к элементу iterable).
        В качестве значений - список элементов итерируемого объекта
        """
        self.groups = {}
        self.func = key
        for item in iterable:
            self.add(item)
        
    def group_for(self, obj):
        return self.func(obj)    
        
    def add(self, item):
        self.groups[self.func(item)] = self.groups.get(self.func(item), []) + [item]
        
    def __contains__(self, key):
        return key in self.groups
        
    def __getitem__(self, key):
        return self.groups[key]
    
    def __len__(self):
        return len(self.groups)
    
    def __iter__(self):
        yield from self.groups.items()

# TEST_1:
grouper = Grouper(['bee', 'geek', 'one', 'two', 'five', 'hi'], key=len)

print(grouper[2])
print(grouper[3])
print(grouper[4])

# TEST_2:
grouper = Grouper(['bee', 'geek', 'one', 'two', 'five', 'hi'], key=len)

print(3 in grouper)
print('bee' in grouper)

# TEST_3:
grouper = Grouper(['hi'], key=lambda s: s[0])
print(len(grouper))

grouper.add('hello')
grouper.add('bee')
grouper.add('big')

print(len(grouper))

grouper.add('geek')
print(grouper['h'])
print(grouper['b'])
print(grouper['g'])

print(len(grouper))

# TEST_4:
grouper = Grouper(['hi'], key=lambda s: s[0])

print(grouper.group_for('hello'))
print(grouper.group_for('bee'))
print(grouper['h'])
print('b' in grouper)

# TEST_5:
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]


grouper = Grouper(persons, key=lambda x: x.height)
print(sorted(grouper))