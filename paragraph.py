from abc import ABC, abstractmethod

class AbstractParagraph(ABC):
    def __init__(self, length):
        self.length = length
        self.data = []
        
    @abstractmethod
    def add(self, words):
        """Добавление слова или нескольких слов, разделенных пробелом, в текущий абзац"""
        
    @abstractmethod
    def end(self):
        """Метод, печатающий абзац, выровненный по левому/правому краю"""
    

class LeftParagraph(AbstractParagraph):
    def add(self, words):
        words = words.split()
        for word in words:
            if self.data and len(self.data[-1]) + len(word) + 1 < self.length:
                self.data[-1] = f"{self.data[-1]} {word}"
            else:
                self.data.append(word)

    def end(self):
        print(*self.data, sep="\n")
        self.data.clear()
    
    
class RightParagraph(AbstractParagraph):
    def add(self, words):
        words = words.split()
        for word in words:
            if self.data and len(self.data[-1]) + len(word) < self.length:
                self.data[-1] = f"{self.data[-1]} {word}"
            else:
                self.data.append(word)
    
    def end(self):
        print(*map(lambda x: x.rjust(self.length), self.data), sep="\n")
        self.data.clear()
     

# TEST_1:
leftparagraph = LeftParagraph(10)

leftparagraph.add('death')
leftparagraph.add('can have me')
leftparagraph.end()
leftparagraph.add('when it earns me')
leftparagraph.end()

# TEST_2:
rightparagraph = RightParagraph(10)

rightparagraph.add('death')
rightparagraph.add('can have me')
leftparagraph.end()
rightparagraph.add('when it earns me')
rightparagraph.end()