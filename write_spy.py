# Задание 7
class WriteSpy:
    def __init__(self, file1, file2, to_close=False):
        """
        Класс осуществляет запись сразу в 2 файла
        file1 - первый файл
        file2 - второй файл
        to_close - если True, то менеджер должен закрыть оба файла, False - оставить открытыми
        """
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args, **kwargs):
        if self.to_close:
            self.close()
    
    def write(self, text):
        """Запись в 2 файла"""
        if not self.writable():
            raise ValueError("Файл закрыт или недоступен для записи")
        self.file1.write(text)
        self.file2.write(text)
        
    def closed(self):
        """Метод возвращает True, если оба файла закрыты, иначе - False """
        return self.file1.closed and self.file2.closed
    
    def writable(self):
        """Метод проверяет доступна ли запись в файл"""
        return (self.file1.mode == "w" and 
                self.file2.mode == "w" and 
                not self.file1.closed and
                not self.file2.closed
                )
    
    def close(self):
        """Закрытие 2 файлов"""
        self.file1.close()
        self.file2.close()

# TEST_1:
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=True) as combined:
    combined.write('You shall seal the blinding light that plagues their dreams\n')
    combined.write('You are the Vessel\n')
    combined.write('You are the Hollow Knight')

print(f1.closed, f2.closed)

with open('file1.txt') as file1, open('file2.txt') as file2:
    print(file1.read())
    print(file2.read())

# TEST_2:
with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.writable())
    
f1 = open('file1.txt')
f2 = open('file2.txt')

with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.writable())

# TEST_3:
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.closed())
    f1.close()
    print(combined.closed())
    f2.close()
    print(combined.closed())

# TEST_4:
f1 = open('file1.txt', mode='r')
f2 = open('file2.txt', mode='w')

try:
    with WriteSpy(f1, f2, to_close=True) as combined:
        combined.write('No cost too great')
except ValueError as error:
    print(error)

# TEST_5:
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')
f1.close()

with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.writable())