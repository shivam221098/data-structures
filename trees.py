"""
    Max Heap
"""
import sys


def parent(pos):
    return pos // 2


def left_child(pos):
    return pos * 2


def right_child(pos):
    return (2 * pos) + 1


class MaxHeap:
    def __init__(self, size):
        self.maxsize = size
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    def is_leaf(self, pos):

        if self.size // 2 <= pos <= self.size:
            return True
        return False

    def swap(self, f_pos, s_pos):
        self.Heap[f_pos], self.Heap[s_pos] = self.Heap[s_pos], self.Heap[f_pos]

    def max_heapify(self, pos):
        if not self.is_leaf(pos):
            if self.Heap[pos] < self.Heap[left_child(pos)] or self.Heap[pos] < self.Heap[right_child(pos)]:
                if self.Heap[left_child(pos)] > self.Heap[right_child(pos)]:
                    self.swap(pos, left_child(pos))
                    self.max_heapify(left_child(pos))

                else:
                    self.swap(pos, right_child(pos))
                    self.max_heapify(right_child(pos))

    def insert(self, data):
        if self.size >= self.maxsize:
            return

        self.size += 1
        self.Heap[self.size] = data

        current = self.size

        while self.Heap[current] > self.Heap[parent(current)]:
            self.swap(current, parent(current))
            current = parent(current)

    def print_heap(self):
        for i in range(1, (self.size // 2) + 1):
            print(f'Parent: {str(self.Heap[i])}, Left child: {self.Heap[2 * i]}, Right child: {self.Heap[2 * i + 1]}')

    def extract_max(self):
        pop = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.max_heapify(self.FRONT)

        return pop


"""
    Min Heap
"""


class MinHeap:
    def __init__(self, size):
        self.maxsize = size
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize * -1
        self.FRONT = 1

    def is_leaf(self, pos):

        if self.size // 2 <= pos <= self.size:
            return True
        return False

    def swap(self, f_pos, s_pos):
        self.Heap[f_pos], self.Heap[s_pos] = self.Heap[s_pos], self.Heap[f_pos]

    def min_heapify(self, pos):
        if not self.is_leaf(pos):
            if self.Heap[pos] > self.Heap[left_child(pos)] or self.Heap[pos] > self.Heap[right_child(pos)]:
                if self.Heap[left_child(pos)] < self.Heap[right_child(pos)]:
                    self.swap(pos, left_child(pos))
                    self.min_heapify(left_child(pos))

                else:
                    self.swap(pos, right_child(pos))
                    self.min_heapify(right_child(pos))

    def insert(self, data):
        if self.size >= self.maxsize:
            return

        self.size += 1
        self.Heap[self.size] = data

        current = self.size

        while self.Heap[current] < self.Heap[parent(current)]:
            self.swap(current, parent(current))
            current = parent(current)

    def print_heap(self):
        for i in range(1, (self.size // 2) + 1):
            print(f'Parent: {str(self.Heap[i])}, Left child: {self.Heap[2 * i]}, Right child: {self.Heap[2 * i + 1]}')

    def min_heap(self):
        for pos in range(self.size // 2, 0, -1):
            self.min_heapify(pos)

    def extract_min(self):
        pop = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.min_heapify(self.FRONT)

        return pop


"""
    Binary Tree
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    else:
        if root.data == data:
            return root
        elif root.data < data:
            root.right = insert(root.right, data)
        else:
            root.left = insert(root.left, data)

    return root


def min_value_node(root):
    current_node = root

    while current_node.left is not None:
        current_node = current_node.left

    return current_node


def delete(root, data):
    if root is None:
        return root

    if data < root.data:
        root.left = delete(root.left, data)

    elif data > root.data:
        root.right = delete(root.right, data)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # In case of two child nodes
        temp = min_value_node(root.right)

        root.data = temp.data

        root.right = delete(root.right, temp.data)

    return root


def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.data, end=" ")
        print_tree(root.right)


if __name__ == '__main__':
    # BT
    root = Node(68)
    root = insert(root, 78)
    root = insert(root, 8)
    root = insert(root, 96)
    root = insert(root, 43)
    root = insert(root, 70)
    root = insert(root, 0)
    root = insert(root, 100)

    print_tree(root)

    print("\n")
    delete(root, 0)

    print_tree(root)

    # MAX HEAP
    print()

    heap = MaxHeap(45)
    heap.insert(3)
    heap.insert(13)
    heap.insert(0)
    heap.insert(67)
    heap.insert(69)
    heap.insert(309)
    heap.insert(90)
    heap.insert(29)

    heap.print_heap()

    print(f'Max Value: {str(heap.extract_max())}')

    # MIN HEAP
    print()

    heap = MinHeap(45)
    heap.insert(3)
    heap.insert(13)
    heap.insert(0)
    heap.insert(67)
    heap.insert(69)
    heap.insert(309)
    heap.insert(90)
    heap.insert(29)

    heap.print_heap()

    print(f'Min Value: {str(heap.extract_min())}')
