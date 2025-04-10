from functools import wraps

def auto_repr(args, kwargs):
    def decorator(cls):
        old_repr = cls.__repr__
        
        @wraps(old_repr)
        def new_repr(self):
            values = [repr(self.__dict__[attr]) for attr in args]
            values += [f"{attr}={repr(self.__dict__[attr])}" for attr in kwargs]
            return f"{cls.__name__}({', '.join(map(str, values))})"
            
        cls.__repr__ = new_repr
        
        return cls
    return decorator


# TEST_1:
@auto_repr(args=['x', 'y'], kwargs=['color'])
class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

point = Point(1, 2, color='green')
print(point)

point.x = 10
point.y = 20
print(point)

# TEST_2:
@auto_repr(args=['name', 'surname'], kwargs=[])
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


person = Person('Gvido', 'van Rossum')
print(person)