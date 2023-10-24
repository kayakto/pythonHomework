class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        if self.start is not None:
            pop_node = self.start
            if self.start.nref is None:
                self.start = self.end = None
                return pop_node.data
            self.start = pop_node.nref
            self.start.pref = None
            return pop_node.data
        return None

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        if self.end is None:
            self.start = self.end = Node(val)
        else:
            end = self.end
            self.end = Node(val)
            self.end.pref = end
            end.nref = self.end


    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        if n == 0:
            new_node = Node(val)
            new_node.nref = self.start
            self.start.pref = new_node
            self.start = new_node
        else:
            current_node = self.start
            index = 0
            while current_node is not None and index < n:
                current_node = current_node.nref
                index += 1
            if current_node is not None:
                new_node = Node(val)
                new_node.pref = current_node.pref
                new_node.nref = current_node
                if current_node.pref is not None:
                    current_node.pref.nref = new_node
                current_node.pref = new_node


    def print(self):
        """
        вывод на печать содержимого очереди
        """
        node = self.start
        while node is not None:
            if node.nref is not None:
                print(node.data, end=", ")
            else:
                print(node.data)
            node = node.nref
