from abc import ABC, abstractmethod

class Validator(ABC):
    def __set_name__(self, owner, name):
        self.name = name
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.name not in instance.__dict__:
            raise AttributeError("Атрибут не найден")
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value
        
    @abstractmethod
    def validate(self, value):
        pass

class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue
        
    def validate(self, obj):
        if type(obj) not in (int, float):
            raise TypeError("Устанавливаемое значение должно быть числом")
        if self.minvalue is not None and obj < self.minvalue:
            raise ValueError(f"Устанавливаемое число должно быть больше или равно {self.minvalue}")
        if self.maxvalue is not None and obj > self.maxvalue:
            raise ValueError(f"Устанавливаемое число должно быть меньше или равно {self.maxvalue}")


class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate
        
    def validate(self, obj):
        if not isinstance(obj, str):
            raise TypeError("Устанавливаемое значение должно быть строкой")
        if self.minsize is not None and len(obj) < self.minsize:
            raise ValueError(f"Длина устанавливаемой строки должна быть больше или равна {self.minsize}")
        if self.maxsize is not None and len(obj) > self.maxsize:
            raise ValueError(f"Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}")
        if self.predicate is not None and not self.predicate(obj):
            raise ValueError("Устанавливаемая строка не удовлетворяет дополнительным условиям")
    
# TEST_1:
class Student:
    age = Number(18, 99)


student = Student()
student.age = 19
print(student.age)

# TEST_2:
class Student:
    age = Number(18, 99)

try:
    student = Student()
    student.age = '19'
except TypeError as error:
    print(error)

# TEST_3:
class Student:
    age = Number(18, 99)

try:
    student = Student()
    student.age = 16
except ValueError as error:
    print(error)

# TEST_4:
class Student:
    age = Number(18, 99)

try:
    student = Student()
    student.age = 101
except ValueError as error:
    print(error)

# TEST_5:
class Person:
    name = String(6, 10)


person = Person()
person.name = 'Андрей'
print(person.name)

# TEST_6:
class Person:
    name = String(6, 10)


person = Person()

try:
    person.name = 'Ян'
except ValueError as e:
    print(e)


try:
    person.name = 'Аполлинария'
except ValueError as e:
    print(e)

try:
    person.name = 1
except TypeError as e:
    print(e)

# TEST_7:
class Person:
    name = String(6, 10, predicate=lambda x: x.startswith('А'))


person = Person()

try:
    person.name = 'Василий'
except ValueError as e:
    print(e)

# TEST_8:
class Student:
    age = Number(18, 99)


student = Student()
try:
    print(student.age)
except AttributeError as e:
    print(e)

# TEST_9:
class Student:
    age = Number(18, 99)

print(Student.age.__class__)