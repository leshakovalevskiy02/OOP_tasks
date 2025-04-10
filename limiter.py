from functools import wraps

def limiter(limit, unique, lookup):
    def decorator(cls):
        cls.limit = limit
        cls.unique_objects = {}
        
        old_method_new = cls.__new__
        old_init = cls.__init__
        
        @wraps(old_method_new)
        def new_method_new(cls, *args, **kwargs):
            obj = old_method_new(cls)
            old_init(obj, *args, **kwargs)
            pk = obj.__dict__[unique]
            if pk in cls.unique_objects:
                return cls.unique_objects[pk]
            if cls.limit > 0:
                cls.unique_objects[pk] = obj
                cls.limit -= 1
                return obj
            if lookup == "FIRST":
                pk, obj = list(cls.unique_objects.items())[0]
            else:
                pk, obj = list(cls.unique_objects.items())[-1]
            return obj
        
        @wraps(old_init)
        def new_init(self, *args, **kwargs):
            pass
        
        cls.__new__ = new_method_new
        cls.__init__ = new_init
        
        return cls
    
    return decorator


# TEST_1:
@limiter(2, 'ID', 'FIRST')
class MyClass:
    def __init__(self, ID, value):
        self.ID = ID
        self.value = value

obj1 = MyClass(1, 5)          # создается экземпляр класса с идентификатором 1
obj2 = MyClass(2, 8)          # создается экземпляр класса с идентификатором 2

obj3 = MyClass(1, 20)         # возвращается obj1, так как экземпляр с идентификатором 1 уже есть
obj4 = MyClass(3, 0)          # превышено ограничение limit, возвращается первый созданный экземпляр

print(obj3.value)
print(obj4.value)

# TEST_2:
@limiter(3, 'ID', 'LAST')
class MyClass:
    def __init__(self, ID, value):
        self.ID = ID
        self.value = value

obj1 = MyClass(1, 5)          # создается экземпляр класса с идентификатором 1
obj2 = MyClass(2, 8)          # создается экземпляр класса с идентификатором 2
obj3 = MyClass(3, 10)         # создается экземпляр класса с идентификатором 3

obj4 = MyClass(4, 0)          # превышено ограничение limit, возвращается последний созданный экземпляр
obj5 = MyClass(2, 20)         # возвращается obj2, так как экземпляр с идентификатором 2 уже есть

print(obj4.value)
print(obj5.value)

# TEST_3:
@limiter(3, 'my_id', 'LAST')
class MyClass:
    def __init__(self, value, my_id):
        self.my_id = my_id
        self.value = value


obj1 = MyClass(12, 0)
obj2 = MyClass(24, 1)
obj3 = MyClass(36, 2)

obj4 = MyClass(48, 3)
obj5 = MyClass(60, 1)

print(obj4 is obj3)
print(obj5 is obj2)