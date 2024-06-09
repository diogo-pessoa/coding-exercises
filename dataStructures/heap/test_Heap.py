from unittest import TestCase

from dataStructures.heap.MaxHeap import MaxHeap


class TestMaxHeap(TestCase):
    def test__left_child(self):
        heap = MaxHeap()
        self.assertEqual(heap._left_child(0), 1)

    def test__right_child(self):
        heap = MaxHeap()
        self.assertEqual(heap._right_child(0), 2)

    def test__parent(self):
        heap = MaxHeap()
        self.assertEqual(heap._parent(1), 0)

    def test__swap(self):
        heap = MaxHeap()
        heap.heap = [1, 2]
        heap._swap(0, 1)
        self.assertEqual(heap.heap, [2, 1])

    def test__heapify(self):
        heap = MaxHeap()
        heap.heap = [1, 2, 3, 5]
        heap._bubble_up()
        self.assertEqual(heap.heap, [5, 1, 3, 2])

    def test_insert(self):
        heap = MaxHeap()
        heap.insert(1)
        heap.insert(2)
        self.assertEqual(heap.heap, [2, 1])

    def test_remove(self):
        heap = MaxHeap()
        heap.insert(1)
        heap.insert(2)
        heap.remove(1)
        self.assertEqual(heap.heap, [2])

    def test_sink_down(self):
        heap = MaxHeap()
        heap.heap = [1, 2, 3, 5]
        heap._sink_down(0)
        self.assertEqual(heap.heap, [5, 2, 3, 1])

    def test_display(self):
        heap = MaxHeap()
        heap.insert(1)
        heap.insert(2)
        self.assertEqual(str(heap), '[2, 1]')
