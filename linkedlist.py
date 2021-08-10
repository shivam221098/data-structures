class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_in_begin(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node

        else:
            node = Node(data)
            node.next = self.head
            self.head = node

    def add_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        i = self.head
        while i.next:
            i = i.next
        i.next = Node(data)

    def insert_list(self, dl):
        self.head = None
        for d in dl:
            self.add_at_end(d)

    def length(self):
        counter = 0
        i = self.head
        while i:
            counter += 1
            i = i.next
        print("\nLength of Linked List is :- ", counter)
        return counter

    def remove_i(self, index):
        if index < 0 or index >= self.length():
            raise Exception("Wrong Index Pointer..")

        if index == 0:
            self.head = self.head.next
            return
        counter = 0
        i = self.head
        while i:
            if counter == index - 1:
                i.next = i.next.next
                break
            i = i.next
            counter += 1

    def insert_at_i(self, index, data):
        if index < 0 or index >= self.length():
            raise Exception("Wrong Index Pointer..")
        if index == 0:
            self.add_in_begin(data)

        counter = 0
        i = self.head
        while i:
            if counter == index - 1:
                node = Node(data)
                i.next = node
                break

            i = i.next
            counter += 1

    def __str__(self):
        if self.head is None:
            print("Empty Linked List... ")
            return
        i = self.head
        linked_list = ''

        while i:
            linked_list += str(i.data) + ', '
            i = i.next
        return linked_list


class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    
class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        node = DNode(data)
        node.next = self.head

        if self.head is not None:
            self.head.prev = node

        self.head = node

    def insert(self, data):

        node = Node(data)

        node.next = None

        if self.head is None:
            node.prev = None
            self.head = node
            return

        last = self.head
        while last.next is not None:
            last = last.next

        last.next = node

        node.prev = last

        return

    def insert_after_node(self, prev, data):
        if prev is None:
            print("Previous node can't be None")
            return

        node = DNode(data)
        node.next = prev.next

        prev.next = node

        node.prev = prev

        if node.next is not None:
            node.next.prev = node

    def show_list(self):
        node = self.head
        last = ''
        print("Forward Direction: ")
        while node is not None:
            print(node.data, end=' ')
            last = node
            node = node.next

        print('\nBackward Direction')

        while last is not None:
            print(last.data, end=' ')
            last = last.prev

    def delete_node(self, node):
        if self.head is None or node is None:
            print("Can't delete")
            return

        if self.head == node:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev

        if node.prev is not None:
            node.prev.next = node.next

        return self.head

    def delete_node_at_i(self, pos):
        if self.head is None or pos <= 0:
            return

        current_node = self.head
        i = 1
        while current_node is not None and i < pos:
            current_node = current_node.next
            i += 1

        if current_node is None:
            return

        self.delete_node(current_node)


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_data(self, data):
        ptr = Node(data)
        temp = self.head

        ptr.next = self.head

        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = ptr

        else:
            ptr.next = ptr
        self.head = ptr

    def show_list(self):
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.data, end=' ')
                temp = temp.next
                if temp == self.head:
                    break


class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            node = DNode(data)
            node.next = node.prev
            self.head = node
            return

        last = self.head.prev

        node = DNode(data)
        node.next = self.head
        self.head.prev = node
        node.prev = last
        last.next = node

    def insert_at_begin(self, data):
        if self.head is None:
            self.head = DNode(data)
            self.head.prev = self.head.next = self.head
            return

        last = self.head.prev
        node = DNode(data)
        node.next = self.head
        node.prev = last
        last.next = self.head.prev = node
        self.head = node

    def insert_after_num(self, num, after):
        node = DNode(num)
        temp = self.head
        while temp.data != after:
            temp = temp.next

        nex = temp.next

        temp.next = node
        node.prev = temp
        node.next = nex
        nex.prev = node

    def show_circular_list(self):
        temp = self.head

        print("Forward Direction: ")
        while temp.next != self.head:
            print(temp.data, end=', ')
            temp = temp.next

        print(temp.data)

        print("Backward Direction: ")
        last = self.head.prev
        temp = last
        while temp.prev != last:
            print(temp.data, end=', ')
            temp = temp.prev

        print(temp.data)


if __name__ == '__main__':
    link_list = LinkedList()
    print("Linked List Values :- ")
    link_list.add_in_begin(5)
    link_list.add_in_begin(1)
    link_list.add_at_end(29)
    link_list.add_in_begin(1000)
    print(link_list)

    link_list.insert_list([5, 6, 44, 64, 4])
    link_list.length()
    link_list.remove_i(3)
    link_list.length()
    link_list.insert_at_i(3, 64)

    print(link_list)

    # Double Linked list
    d_list = DoubleLinkedList()

    d_list.insert(2)
    d_list.insert(40)

    d_list.insert_at_front(90)

    d_list.insert_after_node(d_list.head.next, 8)

    d_list.show_list()
    d_list.delete_node_at_i(3)
    d_list.show_list()

    # Circular linked list
    print()
    c_list = CircularLinkedList()
    c_list.insert_data(12)
    c_list.insert_data(10)
    c_list.show_list()

    # Double Circular Linked List
    print()
    dc_list = CircularDoubleLinkedList()

    dc_list.insert_at_begin(50)
    dc_list.insert_at_begin(89)
    dc_list.insert_at_begin(100)
    dc_list.insert_at_begin(45)
    dc_list.insert_at_begin(101)

    dc_list.insert_at_end(456)
    dc_list.insert_at_end(987)

    dc_list.insert_after_num(78, 456)

    dc_list.show_circular_list()