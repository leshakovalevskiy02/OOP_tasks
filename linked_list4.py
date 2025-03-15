class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        self.__prev = obj

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        """Добавление нового элемента в связный список"""
        if self.head is None:
            self.head = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
        self.tail = obj

    def get_elem_by_index(self, indx):
        """Получение элемента связного списка по индексу"""
        if indx < 0:
            return None
        i = 0
        head = self.head
        while i < indx and head:
            head = head.next
            i += 1
        return head

    def remove_obj(self, indx):
        """Удаление элемента из связного списка по индексу"""
        if self.head is None:
            return
        el = self.get_elem_by_index(indx)
        if el is not None:
            prev_el = el.prev
            next_el = el.next
            el.next = el.prev = None
            
            if prev_el is not None and next_el is None:
                self.tail = prev_el
                prev_el.next = None
                
            elif prev_el is not None and next_el is not None:
                prev_el.next = next_el
                next_el.prev = prev_el
                
            elif prev_el is None and next_el is not None:
                self.head = next_el
                next_el.prev = None
            else:
                self.tail = self.head = None

    def __len__(self):
        ln = 0
        head = self.head
        while head:
            head = head.next
            ln += 1
        return ln

    def __call__(self, indx, *args, **kwargs):
        """При вызове экземпляра класса возвращаются данные элемента свзяного списка по индексу"""
        elem = self.get_elem_by_index(indx)
        if elem is not None:
            return elem.data


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
print(len(linked_lst))  # 3
s1 = linked_lst(0)
s2 = linked_lst(1)
s3 = linked_lst(2)
s4 = linked_lst(-3)
s5 = linked_lst(12)
print(s1, s2, s3, s4, s5)  # Sergey, Balakirev, Python, None, None
linked_lst.remove_obj(2)
print(len(linked_lst))  # 2
s1 = linked_lst(0)
s2 = linked_lst(1)
s3 = linked_lst(2)
print(s1, s2, s3)  # Sergey, Balakirev, None
linked_lst.add_obj(ObjList("Python ООП"))
linked_lst.remove_obj(1)
print(len(linked_lst))  # 2
s1 = linked_lst(0)
s2 = linked_lst(1)
s3 = linked_lst(2)
print(s1, s2, s3)  # Sergey, Python ООП, None
linked_lst.remove_obj(0)
print(len(linked_lst))  # 1
s1 = linked_lst(0)
s2 = linked_lst(1)
s3 = linked_lst(2)
print(s1, s2, s3)  # Python ООП, None, None
linked_lst.remove_obj(0)
print(len(linked_lst))  # 0
s1 = linked_lst(0)
s2 = linked_lst(1)
s3 = linked_lst(2)
print(s1, s2, s3)  # None, None, None
print(linked_lst.head, linked_lst.tail)  # None None
linked_lst.remove_obj(5)