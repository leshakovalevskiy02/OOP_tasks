class LinkedList:
    def __init__(self):
        """
        head - ссылка на первый объект связного списка или None
        tail - ссылка на последний объект связного списка или None
        """
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        """Добавление нового элемента в связный список"""
        if not self.head:
            self.head = obj
        else:
            obj.set_prev(self.tail)
            obj.get_prev().set_next(obj)
        self.tail = obj

    def remove_obj(self):
        """Удаление элемента из связного списка"""
        if self.tail:
            prev_obj = self.tail.get_prev()
            if prev_obj:
                self.tail.set_prev(None)
                prev_obj.set_next(None)
                self.tail = prev_obj
            else:
                self.tail = self.head = None
        else:
            print("В связанном списке нет элементов")

    def get_data(self):
        """Вывод данных data каждого элемента связного списка в виде списка python"""
        data_lst = []
        h_obj = self.head
        while h_obj:
            data_lst.append(h_obj.get_data())
            h_obj = h_obj.get_next()
        return data_lst


class ObjList:
    def __init__(self, data):
        """
        data - переданные данные
        next - ссылка на следующий объект или None
        prev - ссылка на предыдущий объект или None
        """
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

# В степик не вставлять
lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()  
print(res)  # ['данные 1', 'данные 2', 'данные 3']
lst.remove_obj()
res = lst.get_data() 
print(res)  # ['данные 1', 'данные 2']
lst.remove_obj()
res = lst.get_data()
print(res)  # ['данные 1']
lst.remove_obj()
res = lst.get_data()
print(res)  # []
lst.remove_obj()  # В связанном списке нет элементов