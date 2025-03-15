class FieldTracker:
    """Класс позволяет отслеживать состояние атрибутов своих наследников"""
    _init = False
    
    def __init__(self):
        self.changed_values_attrs = {}
            
    def base(self, attr_name):
        """Метод принимающий имя атрибута и возвращающий или текущее значение атрибута,
        или исходное, если оно было изменено"""
        if attr_name not in self.changed_values_attrs:
            return getattr(self, attr_name)
        return self.changed_values_attrs[attr_name]
    
    def has_changed(self, attr_name):
        """Метод принимающий имя атрибута и возвращающий True - если значение было изменено, иначе - False"""
        return attr_name in self.changed_values_attrs
    
    def changed(self):
        """Метод возвращающий словарь, где ключи - атрибуты, которые меняли свое значение,
        значение - их исходное значение"""
        return self.changed_values_attrs
    
    def save(self):
        """Метод сбрасывающий отслеживание. После вызова метода - 
        считается, что все атрибуты ранее не изменяли свои значения, а их текущие зрначения
        - считаются исходными"""
        self.changed_values_attrs = {}
    
    def __setattr__(self, name, value):
        """Магический метод для отслеживания изменения атрибутов"""
        if name == "changed_values_attrs" and not self._init:
            type(self)._init = True
        if name in self.fields and self._init:
            if not self.has_changed(name):
                self.changed_values_attrs[name] = getattr(self, name)
        super().__setattr__(name, value)


# TEST_1:
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()

point = Point(1, 2, 3)

print(point.base('x'))
print(point.has_changed('x'))
print(point.changed())

# TEST_2:
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()

point = Point(1, 2, 3)
point.x = 0
point.z = 4
point.z = 5

print(point.base('x'))
print(point.base('z'))
print(point.has_changed('x'))
print(point.has_changed('z'))
print(point.changed())

# TEST_3:
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()

point = Point(1, 2, 3)
point.x = 0
point.z = 4
point.save()

print(point.base('x'))
print(point.base('z'))
print(point.has_changed('x'))
print(point.has_changed('z'))
print(point.changed())

# TEST_4:
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


p = Point(1, 2, 3)
print(p.changed())
p.x = 4
print(p.changed())
print(p.x)
p.z = 6
print(p.changed())
p.save()
print(p.changed())
p.y = 8
print(p.changed())
print(p.y)
p.save()
print(p.changed())
p.save()
print(p.changed())