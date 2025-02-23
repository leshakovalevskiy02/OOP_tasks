class SortKey:
    def __init__(self, *args):
        """Принимаем на вход произвольное число атрибутов объекта"""
        self.attrs = args
    
    def __call__(self, obj):
        """При вызове как функции для сортировки"""
        return [getattr(obj, attr) for attr in self.attrs]
    
# TEST_1:
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'

users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]

print(sorted(users, key=SortKey('name')))
print(sorted(users, key=SortKey('name', 'age')))
print(sorted(users, key=SortKey('age')))
print(sorted(users, key=SortKey('age', 'name')))

# TEST_2:
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'

users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]

print(max(users, key=SortKey('name')))
print(max(users, key=SortKey('age')))
print(max(users, key=SortKey('name', 'age')))
print(max(users, key=SortKey('age', 'name')))

# TEST_3:
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'

users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]

print(min(users, key=SortKey('name')))
print(min(users, key=SortKey('age')))
print(min(users, key=SortKey('name', 'age')))
print(min(users, key=SortKey('age', 'name')))