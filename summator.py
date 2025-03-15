class Summator:
    """Вычисление суммы чисел от 1 до n"""
    def __init__(self):
        self.m = 1
    
    def total(self, n):
        return sum(map(pow, range(1, n + 1), [self.m] * n))
        
class SquareSummator(Summator):
    """Вычисление суммы квадратов чисел от 1 до n"""
    def __init__(self):
        self.m = 2
    
class QubeSummator(Summator):
    """Вычисление суммы кубов чисел от 1 до n"""
    def __init__(self):
        self.m = 3

class CustomSummator(Summator):
    """Вычисление суммы произвольных степеней чисел от 1 до n"""
    def __init__(self, m):
        self.m = m


# TEST_1:
print(issubclass(SquareSummator, Summator))
print(issubclass(QubeSummator, Summator))

# TEST_2:
summator1 = Summator()
summator2 = SquareSummator()
summator3 = QubeSummator()

print(summator1.total(3))    # 1 + 2 + 3
print(summator2.total(3))    # 1 + 4 + 9
print(summator3.total(3))    # 1 + 8 + 27

# TEST_3:
summator1 = Summator()
summator2 = CustomSummator(2)
summator3 = CustomSummator(3)

print(summator1.total(3))    # 1 + 2 + 3
print(summator2.total(3))    # 1 + 4 + 9
print(summator3.total(3))    # 1 + 8 + 27