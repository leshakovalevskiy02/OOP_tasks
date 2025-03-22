class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, new_data):
        self.__data = new_data
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, obj):
        if type(obj) in (type(None), StackObj):
            self.__next = obj

class Stack:
    def __init__(self):
        """
        self.top - ссылка на элемент, который первым положили в стек
        self.tmp - временная ссылка, для хранения сотояния метода __next__
        self._ln - длина связного списка
        self.i - индекс связного списка, для реализации методов getitem и setitem.
        В случае отсутсвия методов iter и next, python использовал бы метод getitem,
        но было решено разграничить эти методы (пускай сейчас 2-ая логика, но лучше держать контроль
        прохода элементов с помощью итератора в методах специально для этого созданных)
        """
        self.top = self.tmp = None
        self._ln = 0
        self.i = 0
    
    def push_back(self, obj):
        """Добавление нового объекта obj в конец стека"""
        if self.top is None:
            self.top = obj
        else:
            last = self.get_item(len(self) - 1)
            last.next = obj
        self._ln += 1
        
    def push_front(self, obj):
        """Добавление нового объекта obj в начало стека"""
        if self.top is None:
            self.top = obj
        else:
            obj.next = self.top
            self.top = obj
        self._ln += 1
        
    def __correct_indx(self, indx):
        if type(indx) is not int or indx < 0 or indx >= len(self):
            raise IndexError('неверный индекс')
     
    def __len__(self):
        return self._ln
    
    def get_item(self, item):
        self.__correct_indx(item)
        h = self.top
        i = 0
        while i < item:
            i += 1
            h = h.next
        return h
    
    def __getitem__(self, item):
        return self.get_item(item).data
    
    def __setitem__(self, key, value):
        obj = self.get_item(key)
        obj.data = value
        
    def __iter__(self):
        self.tmp = self.top
        return self
    
    def __next__(self):
        obj = self.tmp
        if obj is None:
            raise StopIteration
        self.tmp = obj.next
        return obj