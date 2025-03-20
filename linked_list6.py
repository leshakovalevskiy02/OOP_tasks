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
        if type(obj) in (type(None), StackObj):
            self.__next = obj
            
            
class Stack:
    def __init__(self):
        self.top = self.last = None
        self.ln = 0
        
    def push(self, obj):
        if self.top is None:
            self.top = obj
        else:
            self.last.next = obj
        self.last = obj
        self.ln += 1
        
    def pop(self):
        if self.top is None:
            return 
    
        head = self.top
        while head.next and head.next != self.last:
            head = head.next
            
        res = self.last
        if self.last is head:
            self.top = self.last = None
        else:
            self.last = head
            head.next = None
        self.ln -= 1
        return res
    
    def __correct_indx(self, indx):
        if type(indx) is not int or indx < 0 or indx >= self.ln:
            raise IndexError('неверный индекс')
            
    def __getitem__(self, item):
        self.__correct_indx(item)
        i = 0
        h = self.top
        while i < item:
            h = h.next
            i += 1
        return h
    
    def __setitem__(self, key, value):
        self.__correct_indx(key)
        i = 0
        h = self.top
        prev = None
        while i < key:
            prev = h
            h = h.next
            i += 1
        if prev is None:
            self.top = value
        else:
            prev.next = value
        if h.next is None:
            self.last = value
        else:
            value.next = h.next
            h.next = None
        
    def show(self) -> None:
        tmp = self.top
        while tmp.next is not None:
            print(tmp.data, end=' ')
            tmp = tmp.next
        print(tmp.data)

        
st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
print(st.ln)
print(st.pop().data)
print(st.ln)
print(st.pop().data)
print(st.ln)
print(st.pop().data)
print(st.ln)
print(st.pop())
print("2______________")
st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
print(st[2].data) # obj3
print(st[1].data) # obj2
print(st[0].data) # obj1
try:
    res = st[3] # исключение IndexError
except IndexError as e:
    print(e)
print("3__________")
st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.show() # obj1 obj2 obj3
st[2] = StackObj("new obj3")
st.show() # obj1 obj2 new obj3
st[1] = StackObj("new obj2")
st.show() # obj1 new obj2 new obj3
st[0] = StackObj("trbbt")
st.show() # trbbt new obj2 new obj3
st[0] = StackObj("new obj 1")
st.show() # new obj 1 new obj2 new obj3
st.pop()
st.pop()
st.show() # new obj 1
st[0] = StackObj("a")
st.show() # a