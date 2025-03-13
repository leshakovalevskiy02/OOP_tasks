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
        if isinstance(obj, (StackObj, type(None))):
            self.__next = obj


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        """
        Метод добавления нового элемента в связный список
        """
        if self.top is None:
            self.top = obj
        else:
            head = self.top
            while head.next is not None:
                head = head.next
            head.next = obj

    def get_data(self):
        """
        Метод получение всех элементов связного списка
        """
        lst_data = []
        head = self.top
        while head:
            lst_data.append(head.data)
            head = head.next
        return lst_data

    def pop(self):
        """
        Метод для удаления элемента из конца связного списка и возврат его
        """
        head = self.top
        if head is None:
            return
        prev_obj = None
        while head.next is not None:
            prev_obj = head
            head = head.next
        if prev_obj is not None:
            prev_obj.next = None
        else:
            self.top = None
        return head
    
st = Stack()
st.push(StackObj("obj1"))
print(st.get_data())
st.push(StackObj("obj2"))
print(st.get_data())
st.push(StackObj("obj3"))
print(st.get_data())
print(st.pop())  # head3
print(st.pop())  # head2
print(st.pop())  # head1
print(st.pop())  # None