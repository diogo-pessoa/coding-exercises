class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self, data):
        node = Node(data)
        self.head = node
        self.tail = node
        self.size = 1

    def append(self, data):
        """
        O(1)
        :param data:
        :return:
        """
        new_node = Node(data)

        self.tail.next = new_node  # current tail points to new node
        new_node.prev = self.tail  # new node previous points to current tail
        self.tail = new_node  # update ll tail to new node
        self.size += 1  # bump size

    def pop(self):
        """
        O(1)
        :return:
        """

        if self.size == 0:
            return None
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return None
        new_tail = self.head
        while new_tail.next is not self.tail:
            new_tail = new_tail.next
        self.tail = new_tail
        self.tail.next = None
        self.size -= 1
        return True

    def prepend(self, data):
        """
        O(1)
        :param data:
        :return:
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size += 1
        return True

    def pop_first(self):
        """
        O(1)
        :return:
        """
        if self.size == 0:
            return None
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return None
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
        return True

    def get_node(self, index):
        """
        O(n)
        :param index:
        :return:
        """
        if index < 0 or index >= self.size:
            return None

        # for a doubly linked list, we can traverse from the head or tail,
        # we can evaluate the index against the length of the list
        if index < self.size // 2: # if index is less than half the size of the list, traverse from the head
            node = self.head
            for i in range(index):
                node = node.next
        else: # if index is greater than half the size of the list, traverse from the tail
            node = self.tail
            for i in range(self.size - 1, index, -1):
                node = node.prev
        return node

    def set_value_at_index(self, index, data):
        """
        O(n)
        :param index:
        :param data:
        :return:
        """
        node = self.get_node(index) # O(n)
        if node:
            node.data = data
            return True
        return False

    def insert_new_node(self, data, index):
        """
        O(n)
        :param data:
        :param index:
        :return:
        """
        if index < 0 or index >= self.size:
            return False
        if index == 0:
            return self.prepend(data)
        if index == self.size:
            return self.append(data)
        current_node = self.get_node(index - 1)
        new_node = Node(data)
        new_node.next = current_node.next
        new_node.prev = current_node
        current_node.next.prev = new_node
        current_node.next = new_node
        self.size += 1
        return True

    def remove_node(self, index):
        """
        O(n)
        :param index:
        :return:
        """
        if index < 0 or index >= self.size:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.size - 1:
            return self.pop()
        node = self.get_node(index)
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return True

    def __str__(self):
        """
        O(n)
        :return:
        """
        if self.size == 0:
            return "Empty list"
        current_node = self.head
        output = []
        while current_node:
            output.append(current_node.data)
            current_node = current_node.next
        return f"{' -> '.join(map(str, output))}"
