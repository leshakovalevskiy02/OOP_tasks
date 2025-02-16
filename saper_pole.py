import random


class Cell:
    def __init__(self, around_mines=0, mine=False, fl_open=False):
        """
        around_mines - число мин вокруг клетки
        mine - наличие/отсутствие мины в текущей клетке
        fl_open - открыта или закрыта клетка
        """
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    def __init__(self, N, M):
        """
        N - размер поля
        M - количество мин
        """
        self.pole = [[Cell() for _ in range(N)] for _ in range(N)]
        self.M = M
        self.init()

    def init(self):
        tpl_shift = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        n = len(self.pole)
        while self.M:
            i_ind = random.randrange(n)
            j_ind = random.randrange(n)
            if not self.pole[i_ind][j_ind].mine:
                self.pole[i_ind][j_ind] = Cell(around_mines=0, mine=True)
                for i_shift, j_shift in tpl_shift:
                    res_i = i_ind + i_shift
                    res_j = j_ind + j_shift
                    if 0 <= res_i < n and 0 <= res_j < n:
                        if not self.pole[res_i][res_j].mine:
                            self.pole[res_i][res_j] = Cell(self.pole[res_i][res_j].around_mines + 1)
                self.M -= 1

    def show(self):
        for row in self.pole:
            for el in row:
                if el.fl_open:
                    print(str(el.around_mines).rjust(3), end="")
                else:
                    print("#".rjust(3), end="")
            print()


pole_game = GamePole(10, 12)
for row in pole_game.pole:
    for el in row:
        el.fl_open = True  # делаем все клетки открытыми
pole_game.show()  # показ игрового поля