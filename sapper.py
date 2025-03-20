import random


class Cell:
    def __init__(self):
        """
        __is_mine - булево значение True/False; True - в клетке находится мина, False - мина отсутствует;
        __number - число мин вокруг клетки (целое число от 0 до 8);
        __is_open - флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.
        """
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False
        
    @classmethod
    def __correct_flag(cls, value):
        if type(value) is not bool:
            raise ValueError("недопустимое значение атрибута")
            
    @classmethod
    def __correct_num(cls, value):
        if type(value) is not int or value < 0 or value > 8:
            raise ValueError("недопустимое значение атрибута")
    
    @property
    def is_mine(self):
        return self.__is_mine
    
    @is_mine.setter
    def is_mine(self, is_m):
        self.__correct_flag(is_m)
        self.__is_mine = is_m
        
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, num):
        self.__correct_num(num)
        self.__number = num
        
    @property
    def is_open(self):
        return self.__is_open
    
    @is_open.setter
    def is_open(self, is_open):
        self.__correct_flag(is_open)
        self.__is_open = is_open
    
    def __bool__(self):
        """Возвращает True, если клетка закрыта и False - если открыта"""
        return not self.is_open


class GamePole:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        """Можно создать только одно поле для игры Сапер"""
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    @classmethod
    def set_flag(cls):
        cls._instance = None
        
    def __del__(self):
        self.set_flag()
    
    def __init__(self, N, M, total_mines):
        """__pole_cells - двумерный (вложенный) кортеж, размерами N x M элементов, состоящий из объектов класса Cell"""
        self.n = N
        self.m = M
        self.__pole_cells = tuple(tuple(Cell() for j in range(M)) for i in range(N))
        self.total_mines = total_mines
        self.init_pole()
        
    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        """Инициализации начального состояния игрового поля (расставляет мины и делает все клетки закрытыми)"""
        tpl_shift = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        n = self.n
        m = self.m
        while self.total_mines:
            i_ind = random.randrange(n)
            j_ind = random.randrange(m)
            if not self.pole[i_ind][j_ind].is_mine:
                self.pole[i_ind][j_ind].is_mine = True
                self.pole[i_ind][j_ind].number = 0
                for i_shift, j_shift in tpl_shift:
                    res_i = i_ind + i_shift
                    res_j = j_ind + j_shift
                    if 0 <= res_i < n and 0 <= res_j < m:
                        if not self.pole[res_i][res_j].is_mine:
                            self.pole[res_i][res_j].number += 1
                self.total_mines -= 1
                
    def open_cell(self, i, j):
        """Открывает ячейку с индексами (i, j); нумерация индексов начинается с нуля;
        метод меняет значение атрибута __is_open объекта Cell в ячейке (i, j) на True"""
        if 0 <= i < self.n and 0 <= j < self.m:
            self.pole[i][j].is_open = True
        else:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def show_pole(self):
        """Отображает игровое поле в консоли"""
        for row in self.pole:
            for el in row:
                if el.is_open:
                    print(str(el.number).rjust(3), end="")
                else:
                    print("#".rjust(3), end="")
            print()

p = GamePole(10, 20, 10)
p2 = GamePole(1, 2, 1)
print(id(p), id(p2))

pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
pole.show_pole()
try:
    pole.open_cell(30, 100)  # генерируется исключение IndexError
except IndexError as e:
    print(e)