class TreeObj:
    def __init__(self, indx, value=0):
        """
        indx - проверяемый в вершине дерева индекс вектора x
        value - значение, хранящееся в вершине (принимает значение None для вершин, у которых есть потомки - промежуточных вершин)
        __left и __right левый и правый потомки узла решающего дерева
        """
        self.indx = indx
        self.value = value
        self.__left = self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value


class DecisionTree:
    @classmethod
    def predict(cls, root, x):
        """
        Построение прогноза (прохода по решающему дереву) для вектора x из корневого узла дерева root.
        Возвращает значение узла - атрибут value
        """
        node = root
        while node:
            value = x[node.indx]
            if value:
                next_node = node.left
            else:
                next_node = node.right
            if next_node is None:
                break
            node = next_node
        return node.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        """
        Добавление вершин в решающее дерево.
        Возвращает добавленную вершину - объект класса TreeObj
        """
        if node is not None:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x)  # будет программистом
print(res)