class MaxHeap:

    def __init__(self):
        self.heap = []

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _parent(self, i):

        return (i - 1) // 2

    def _swap(self, i, j):
        """
        Swap two elements in the heap
        :param i:
        :param j:
        :return:
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _bubble_up(self):
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):

        max_index = index
        left_child = self._left_child(index)
        right_child = self._right_child(index)
        while True:
            if len(self.heap) > left_child > self.heap[index]:
                max_index = left_child
            if len(self.heap) > right_child > self.heap[index]:
                max_index = right_child
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def insert(self, value):
        self.heap.append(value)
        self._bubble_up()

    def remove(self, value):
        """
        Remove a value from the heap, you'll only ever remove the root node.

        :param value:
        :return:
        """
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        # the pop method returns the removed element, which we use as an argument to
        # insert at the top of the heap.
        self.heap[0] = self.heap.pop()
        # now call sink_down to move the new root to its correct position
        self._sink_down(0)

    def __str__(self):
        return str(self.heap)
