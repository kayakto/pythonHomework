class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел


class Stack:
    """
    Основной класс для стека
    """
    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        """

        if self.end is not None:
            pop_data = self.end.data
            self.end = self.end.pref
            return pop_data
        return None

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_node = Node(val)
        new_node.pref = self.end
        self.end = new_node

    def print(self):
        """
        вывод на печать содержимого стека
        """
        current_node = self.end
        while current_node is not None:
            if current_node.pref is not None:
                print(current_node.data, end=", ")
            else:
                print(current_node.data)
            current_node = current_node.pref


