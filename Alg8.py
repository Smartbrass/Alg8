# Класс для хранения узла BST.
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Функция для выполнения неупорядоченного обхода BST
def inorder(root):
    if root is None:
        return
 
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)
 
 
# Вспомогательная функция # для поиска узла минимального значения в поддереве с корнем в `curr`
def getMinimumKey(curr):
    while curr.left:
        curr = curr.left
    return curr
 
 
# Рекурсивная функция для вставки ключа в BST
def insert(root, key):
 
    #, если корень None, создайте новый узел и верните его.
    if root is None:
        return Node(key)
 
    #, если данный ключ меньше корневого узла, повторить для левого поддерева
    if key < root.data:
        root.left = insert(root.left, key)
 
    #, если данный ключ больше, чем корневой узел, повторить для правого поддерева
    else:
        root.right = insert(root.right, key)
 
    return root
 
 
# Функция удаления узла из BST
def deleteNode(root, key):
 
    # Указатель # для хранения родителя текущего узла
    parent = None
 
    # запускается с корневого узла
    curr = root
 
    # Ключ поиска # в BST и установка его родительского указателя
    while curr and curr.data != key:
 
        # обновляет родителя до текущего узла
        parent = curr
 
        #, если данный ключ меньше текущего узла, перейти к левому поддереву;
        # иначе перейти к правому поддереву
        if key < curr.data:
            curr = curr.left
        else:
            curr = curr.right
 
    # возврат, если ключ не найден в дереве
    if curr is None:
        return root
 
    # Случай 1: удаляемый узел не имеет потомков, т. е. это конечный узел.
    if curr.left is None and curr.right is None:
 
        #, если удаляемый узел не является корневым узлом, то установите его
        # родительский левый/правый дочерний в None
        if curr != root:
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None
 
        #, если дерево имеет только корневой узел, установите для него значение «Нет».
        else:
            root = None
 
    # Случай 2: удаляемый узел имеет двух дочерних элементов
    elif curr.left and curr.right:
 
        # находит свой неупорядоченный узел-преемник
        successor = getMinimumKey(curr.right)
 
        # сохраняет значение преемника
        val = successor.data
 
        # рекурсивно удаляет преемника. Обратите внимание, что преемник
        # будет иметь не более одного дочернего элемента (правый дочерний элемент)
        deleteNode(root, successor.data)
 
        # копирует значение преемника в текущий узел
        curr.data = val
 
    # Случай 3: удаляемый узел имеет только одного потомка
    else:
 
        # выбирает дочерний узел
        if curr.left:
            child = curr.left
        else:
            child = curr.right
 
        #, если удаляемый узел не является корневым узлом, установим его родительский
        # своему потомку
        if curr != root:
            if curr == parent.left:
                parent.left = child
            else:
                parent.right = child
 
        #, если удаляемый узел является корневым узлом, то установим корень в дочерний
        else:
            root = child
 
    return root
 
 
if __name__ == '__main__':
 
    keys = [15, 10, 20, 8, 12, 16]
 
    root = None
    for key in keys:
        root = insert(root, key)
 
    root = deleteNode(root, 8)
    inorder(root)
 