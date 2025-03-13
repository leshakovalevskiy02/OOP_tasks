class Versioned:
    def __init__(self):
        """
        self._versioned - хранит в качестве ключа - объект класса, который использует дескриптор Versioned,
        в качестве значения - список значений, которые принимает свойство объекта класса.
        """
        self._versions = {}
        
    def __set_name__(self, owner, name):
        """
        Создание дескриптора для защищенного свойства
        """
        self.name = "_" + name
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.name in instance.__dict__:
            return getattr(instance, self.name)
        raise AttributeError("Атрибут не найден")
    
    def __set__(self, instance, value):
        self._versions[instance] = self._versions.get(instance, []) + [value]
        setattr(instance, self.name, value)
    
    def get_version(self, instance, n):
        return self._versions[instance][n - 1]
    
    def set_version(self, instance, n):
        setattr(instance, self.name, self._versions[instance][n - 1])
        
# TEST_1:
class Student:
    age = Versioned()
    
student = Student()

student.age = 18
student.age = 19
student.age = 20

print(student.age)
print(Student.age.get_version(student, 1))
print(Student.age.get_version(student, 2))
print(Student.age.get_version(student, 3))

# TEST_2:
class Student:
    age = Versioned()
    
student = Student()

student.age = 18
student.age = 19
student.age = 20

print(student.age)
Student.age.set_version(student, 1)
print(student.age)

# TEST_3:
class Student:
    name = Versioned()

student = Student()

try:
    print(student.name)
except AttributeError as e:
    print(e)

# TEST_4:
class Student:
    age = Versioned()


student1 = Student()
student2 = Student()

student1.age = 18
student1.age = 19
student1.age = 20

student2.age = 30
student2.age = 31
student2.age = 32

print(student1.age)
print(student2.age)
Student.age.set_version(student1, 1)
Student.age.set_version(student2, 2)
print(student1.age)
print(student2.age)

# TEST_5:
class Student:
    age = Versioned()


student = Student()

student.age = 18
student.age = 19
student.age = 20

print(student.age)

Student.age.set_version(student, 1)

print(student.age)
for i in range(3):
    print(Student.age.get_version(student, i + 1))

Student.age.set_version(student, 2)

print(student.age)
for i in range(3):
    print(Student.age.get_version(student, i + 1))

# TEST_6:
class Student:
    age = Versioned()

print(Student.age.__class__)