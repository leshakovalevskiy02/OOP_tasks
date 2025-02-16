import sys


class ListObject:
    def __init__(self, data):
        """
        data - строка с данными
        next_obj - ссылка на следующий объект или None
        """
        self.data = data
        self.next_obj = None

    def link(self, obj):
        """Добавление нового объекта в связный список"""
        self.next_obj = obj

lst_in = list(map(str.strip, sys.stdin.readlines())) # Считывание строк из потока

# Добавление элементов в связный список
head_obj = ListObject(lst_in[0])
prev_obj = head_obj
for i in range(1, len(lst_in)):
    head_obj.link(ListObject(lst_in[i]))
    head_obj = head_obj.next_obj
head_obj = prev_obj

# Вывод строки текста каждого объекта связного списка
while head_obj.next_obj:
    print(head_obj.data)
    head_obj = head_obj.next_obj
print(head_obj.data)