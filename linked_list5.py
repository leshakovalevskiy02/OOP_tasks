class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

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
        self.last = None
        
    def push_back(self, obj):
        """Добавление элемента в связный список"""
        if self.top is None:
            self.top = obj
        else:
            self.last.next = obj
        self.last = obj
        
    def get_data(self):
        """Возвращение данных всем элементов связного списка"""
        head = self.top
        lst = []
        while head is not None:
            lst.append(head.data)
            head = head.next
        return lst
    
    def __add__(self, other):
        """Добавление нового элемента в связный список для операций + и +="""
        self.push_back(other)
        return self
    
    def __mul__(self, other):
        """Добавление новых элементов в связный список для операций * и *="""
        for el in other:
            self.push_back(StackObj(el))
        return self
    
    def pop_back(self):
        """Удаление последнего элемента из связного списка"""
        if self.top is None:
            return
        head = self.top
        while head.next is not None and head.next != self.last:
            head = head.next
            
        if self.top == self.last:
            self.top = self.last = None    
        else:
            self.last = head
            head.next = None

        
h = StackObj('5')
print(h.data) # 5
st = Stack()
st.push_back(StackObj('1'))
st.push_back(StackObj('2'))
st.push_back(StackObj('3'))
print(st.get_data()) # 1 2 3
st = st + StackObj('4')
st += StackObj('5')
print(st.get_data()) # 1 2 3 4 5
st = st * [str(i) for i in range(6, 9)]
st *= [str(i) for i in range(9, 12)]
print(st.get_data())  # 1 2 3 4 5 6 7 8 9 10 11 12
for i in range(12):
    st.pop_back()
    print(st.get_data())