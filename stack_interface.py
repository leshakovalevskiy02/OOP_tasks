from abc import ABC, abstractmethod

class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        """Добавление объекта в конец стека"""
        
    @abstractmethod
    def pop_back(self):
        """Удаление последнего объекта из стека"""
        
class Stack(StackInterface):
    def __init__(self):
        self._top = None
          
    def push_back(self, obj):
        if self._top is None:
            self._top = obj
        else:
            head = self._top
            while head._next:
                head = head._next
            head._next = obj
            
    def pop_back(self):
        if self._top is None:
            return
        
        prev_head = None
        head = self._top
        while head._next:
            prev_head = head
            head = head._next
            
        if prev_head is None:
            self._top = None
            return head
        
        prev_head._next = None
        return head
        
        
class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None

st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
del_obj = st.pop_back() # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
del_obj = st.pop_back()
del_obj = st.pop_back()
st.push_back(StackObj("obj 3"))
print(del_obj)
print(st._top._data)