# PROGRAM(WORKING ON LIST):
# starting with list


# Initialising a list
name = []

# inserting values in a list using insert function
print('Inserting values in a list using insert function :- ')
name.insert(0, 'Rida')
name.insert(0, 'Ali')
print(name, '\n')
# inserting values in a list using append function
print('inserting values in a list using append function :- ')
name.append('Khan')
print(name, '\n')

# Deleting values from a list using remove
print('Deleting values from a list using remove function :- ')
name.remove('Ali')
print(name, '\n')

# Deleting values from a list using POP
print('Deleting values from a list using POP function :- ')
name.remove('Khan')
print(name, '\n')

# searching in list
print('Searching in list :- ')
for i in name:
    if i == 'Rida':
        print("Found Name 'Rida' in List.")
    else:
        print("Not Found")

# updating list
print('\nUpdating list :- ')
name[0] = 'Ali'
print(name)

# Lab No 3 (All Sortings In One Program):


# Initialising a list and assigning values
nums = [5, 9, 8, 7, 6, 0]


# function for Bubble Sort
def bub_sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
    print("Bubble Sort Method :- ", nums)


# function for Selection Sort
def selc_sort(nums):
    for i in range(5):
        mine = i
        for j in range(i, 6):
            if nums[j] < nums[mine]:
                mine = j
        temp = nums[i]
        nums[i] = nums[mine]
        nums[mine] = temp

    print("Selection Sort Method :- ", nums)


# function for Shell Sort
def shell_sort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2


def foo(arr):
    size = len(arr)
    gap = size // 2
    gap = 3
    for i in range(gap, size):
        anchor = arr[i]
        j = i
        while j >= gap and arr[j - gap] > anchor:
            arr[j] = arr[j - gap]
            j -= gap
        arr[j] = anchor


# function for Insertion Sort
def insertion_sort(nums):
    for i in range(1, len(nums)):
        anchor = nums[i]
        j = i - 1
        while j >= 0 and anchor < nums[j]:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = anchor
    print("Insertion Sort Method :- ", nums)


# function for Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)


def merge_two_sorted_lists(a, b, arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


# function for quick sort
def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


bub_sort(nums)
selc_sort(nums)
shell_sort(nums)
print("Shell Sort Method :- ", nums)
insertion_sort(nums)
merge_sort(nums)
print("Merge Sort Method :- ", nums)
quick_sort(nums, 0, len(nums) - 1)
print("Quick Sort Method :- ", nums)

# Queue program


# Initializing a queue
# taking example a friend queue
rida_friends = []

# Adding elements to the queue using append function
rida_friends.append('Sam')
rida_friends.append('john')
rida_friends.append('umrao')
rida_friends.append('Stephen')
rida_friends.append('Bravo')

print("Queue after adding Elements into it")
print(rida_friends)

# Removing elements from the queue
print("\nRemoving Elements One By One from Queue (FIFO).\n")
for i in range(0, len(rida_friends)):
    print("Removed ", f"'{rida_friends.pop(0)}'", " in this iteration.")
    print(rida_friends, '\n')

# TASK NO 5 (STACK)
# Initializing a Stack
# taking example a friend Stack
rida_friends = []

# Adding elements to the Stack using append function
rida_friends.append('Sam')
rida_friends.append('john')
rida_friends.append('umrao')
rida_friends.append('Stephen')
rida_friends.append('Bravo')

print("Stack after adding Elements into it.")
print(rida_friends)

# Removing elements from the Stack
print("\nRemoving Elements One By One from Stack (LIFO).\n")
for i in range(0, len(rida_friends)):
    print("Removed ", f"'{rida_friends.pop()}'", " in this iteration.")
    print(rida_friends, '\n')


# TASK NO 6 (Linked List)
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



# TASK NO 7 (STRING OPERATIONS):

print('\nString operations in python ::')

# initializing a string

name = 'Hii I Am Rida Khan'
print("Default String :- ", name, "\n\n")

# Capitalizing a string
x = name.capitalize()
print("Capitalized String :- ", x)

# converts to case folded string
x = name.casefold()
print("\nCase folded String :- ", x)

# returns occurrences of substring in string
x = name.count('a')
print("\nNumber of Occurrences of 'a' in string :- ", x)

# Checks if String Ends with the Specified Suffix
x = name.endswith('n')
print("\nIf string is ending with letter 'n' or not :- ", x)

# Returns the lower string
x = name.lower()
print("\nLower String :- ", x)

# Encoded String
x = name.encode()
print("\nEncoded String :- ", x)

# Checking Alpha String
x = name.isalpha()  # Returns False because of spaces between words in string
print("\nChecking Alpha String :- ", x)

# Doing string Partitions
x = name.partition(name)
print("\nDoing string Partitions", x)

x = name.rfind('Khan')
print("\nReturning index where 'Khan' was lastly found :- ", x)

# if starts with 'H'.
x = name.startswith('H')
print("\nif starts with 'H' :- ", x)
