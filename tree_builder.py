class TreeBuilder:
    """
    __ID - уровень вложенности элемента
    """
    __ID = 0
    
    def __init__(self):
        self.__data = [[]]

    def add(self, least):
        lst = self.get_list_by_index(self.__ID)
        lst[-1].append(least)
    
    def structure(self):
        return self.__data[0]
    
    def get_list_by_index(self, index):
        lst = self.__data
        for _ in range(index):
            for obj in lst:
                if type(obj) == list:
                    lst = obj
        return lst
    
    @classmethod
    def inc_id(cls):
        cls.__ID += 1
        
    @classmethod
    def dec_id(cls):
        cls.__ID -= 1
                    
    def __enter__(self):
        """
        При вызове менеджера контекста, уровень вложенности увеличается на 1
        """
        self.inc_id()
        lst = self.get_list_by_index(self.__ID)
        lst.append([])
        return self
    
    def __exit__(self, *args, **kwargs):
        """
        При закрытии менеджера контекста, уровень вложенности уменьшается на 1.
        Если есть уровни вложенности не содержащие элементов они удаляются
        """
        lst = self.get_list_by_index(self.__ID)[-1]
        prev_lst = self.get_list_by_index(self.__ID)
        if lst == []:
            prev_lst.remove(lst)
        self.dec_id()
        return 1

# TEST_1:
tree = TreeBuilder()
print(tree.structure())

tree.add('1st')
print(tree.structure())

with tree:
    tree.add('2nd')
    with tree:
        tree.add('3rd')
    tree.add('4th')
    with tree:
        pass
        
print(tree.structure())

# TEST_2:
tree = TreeBuilder()

tree.add('1st')

with tree:
    tree.add('2nd')
    with tree:
        tree.add('3rd')
        with tree:
            tree.add('4th')
            with tree:
                tree.add('5th')
    with tree:
        pass

tree.add('6th')
print(tree.structure())

# TEST_3:
tree = TreeBuilder()

with tree:
    tree.add(1)
    tree.add(2)
    with tree:
        tree.add(3)
        with tree:
            tree.add(4)
    with tree:
        tree.add(5)

print(tree.structure())

# TEST_4:
tree = TreeBuilder()

with tree:
    tree.add(1)
    with tree:
        tree.add(2)
        tree.add(3)
    with tree:
        pass

print(tree.structure())

# TEST_5:
tree = TreeBuilder()

tree.add(0)
print(tree.structure())

with tree:
    tree.add(1)
    with tree:
        tree.add(2)
        tree.add(3)
        with tree:
            tree.add(4)
    with tree:
        pass

print(tree.structure())

with tree:
    tree.add(5)
    with tree:
        tree.add(6)
    with tree:
        tree.add(7)
        with tree:
            tree.add(8)

print(tree.structure())

# TEST_6:
tree = TreeBuilder()

tree.add('root')
with tree:
    tree.add('first child')
    tree.add('second child')
    with tree:
        tree.add('grandchild')
    tree.add('bastard')
    with tree:
        pass
    tree.add('another bastard')

print(tree.structure())

# TEST_7:
tree = TreeBuilder()

tree.add('1st')

with tree:
    with tree:
        with tree:
            with tree:
                tree.add('5th')

print(tree.structure())

# TEST_8:
tree1 = TreeBuilder()
tree2 = TreeBuilder()

tree1.add('1st')

with tree1:
    tree1.add('2nd')
    with tree1:
        tree1.add('3rd')
    tree1.add('4th')
    with tree1:
        pass

print(tree1.structure())
print(tree2.structure())