class TicTacToe:
    def __init__(self):
        self._n = 3
        self.pole = tuple(tuple(Cell() for j in range(self._n)) for i in range(self._n))
        
    def clear(self):
        for row in self.pole:
            for el in row:
                el.value = 0
                el.is_free = True
                
    def __correct_indx(self, indx):
        if type(indx) is not int or indx < 0 or indx >= self._n:
            raise IndexError('неверный индекс клетки')
            
    def __is_free(self, ind1, ind2):
        if not bool(self.pole[ind1][ind2]):
            raise ValueError('клетка уже занята')
                
    def __getitem__(self, item):
        """
        Метод позволяет обращаться к объекту следующим образом:
        res = game[1, 1] # получение значения центральной ячейки поля (возвращается число)
        slice_1 = game[:, indx] # выбираются все элементы (кортеж) столбца с индексом indx
        slice_2 = game[indx, :] # выбираются все элементы (кортеж) строки с индексом indx
        """
        i, j = item
        if type(i) is not slice:
            self.__correct_indx(i)
        if type(j) is not slice:
            self.__correct_indx(j)
        if type(i) is slice:
            res = list(zip(*self.pole))[j][i]
            return tuple(item.value for item in res)
        if type(j) is slice:
            res = self.pole[i][j]
            return tuple(item.value for item in res)
        return self.pole[i][j].value
        
    def __setitem__(self, key, value):
        """
        Возможность обращаться к элементам поля, следующим образом
        game[0, 0] = 1
        Обращение к занятой клетке приводит к исключению
        """
        i, j = key
        self.__correct_indx(i)
        self.__correct_indx(j)
            
        self.__is_free(i, j)
        self.pole[i][j].value = value
        self.pole[i][j].is_free = False

class Cell:
    def __init__(self):
        """
        is_free - True, если клетка свободна; False в противном случае(по умолчанию - свободна)
        value - значение поля: 1 - крестик; 2 - нолик (по умолчанию 0).
        """
        self.is_free = True
        self.value = 0
        
    def __bool__(self):
        """Возвращает True, если клетка свободна"""
        return self.is_free
    
    
game = TicTacToe()
game.clear()
game[0, 0] = 1
game[1, 0] = 2
# формируется поле:
# 1 0 0
# 2 0 0
# 0 0 0
try:
    game[3, 2] = 2 # генерируется исключение IndexError
except IndexError as e:
    print(e)
if game[0, 0] == 0:
    game[0, 0] = 2
v1 = game[0, :]  # 1, 0, 0
print(v1)
v2 = game[:, 0]  # 1, 2, 0
print(v2)
v3 = game[:2, 0]
print(v3)  # (1, 2)
game[2, 0] = 3
v4 = game[:, 0]
print(v4)