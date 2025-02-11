class Knight:
    """
    Класс описывающий шахматного коня.
    """
    def __init__(self, horizontal, vertical, color):
        """
        Метод принимает клетку шахматной доски по вертикали и горизонтали,
        например "c3" и цвет коня
        """
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        
    def get_char(self):
        return "N"
    
    def can_move(self, horizontal, vertical):
        """
        Метод проверяющий может ли конь перепрыгнуть к переданную клетку
        """
        horizontal_diference = ord(horizontal) - ord(self.horizontal)
        vertical_diference = vertical - self.vertical
        if abs(horizontal_diference) == 2 and abs(vertical_diference) == 1 or \
            abs(vertical_diference) == 2 and abs(horizontal_diference) == 1:
                return True
        return False
    
    def move_to(self, horizontal, vertical):
        """
        Метод перемещающий коня в заданную клетку
        """
        if self.can_move(horizontal, vertical):
            self.horizontal = horizontal
            self.vertical = vertical
    
    def draw_board(self):
        """
        Метод для отрисовки шахматного поля, позиции коня и вариантов его хода 
        """
        for i in range(8, 0, -1):
            for j in range(ord("a"), ord("h") + 1):
                if chr(j) == self.horizontal and i == self.vertical:
                    print(self.get_char(), end="")
                elif self.can_move(chr(j), i):
                    print("*", end="")
                else:
                    print(".", end="")
            print()
        


knight = Knight('c', 3, 'white')


print(knight.color, knight.get_char())
print(knight.horizontal, knight.vertical)


knight = Knight('c', 3, 'white')

print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

knight.move_to('e', 4)
print(knight.horizontal, knight.vertical)

knight = Knight("a", 1, "white")
knight.draw_board()
knight.can_move("b", 3)
print()
knight.move_to("b", 3)
knight.move_to("d", 4)
knight.draw_board()
print(knight.vertical, knight.horizontal)