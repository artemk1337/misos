from random import randint


arr_ = [randint(0, 1000) for i in range(25)]
SIZE = 25


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.nextNode = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head is None or data < self.head.data:
            newNode.nextNode = self.head
            self.head = newNode
        else:
            current = self.head
            while current.nextNode is not None and current.nextNode.data < data:
                current = current.nextNode
            newNode.nextNode = current.nextNode
            current.nextNode = newNode


def hashFunction(num, maximum):
    # Адрес от 0 до SIZE
    address = int((num * 1.0 / maximum) * (SIZE - 1))
    return address


def addressCalculationSort(arr):
    listOfLinkedLists = []
    for i in range(SIZE):
        listOfLinkedLists.append(LinkedList())
    maximum = max(arr)
    for val in arr:
        address = hashFunction(val, maximum)
        listOfLinkedLists[address].insert(val)
    index = 0
    for i in range(SIZE):
        current = listOfLinkedLists[i].head
        while current:
            arr[index] = current.data
            index += 1
            current = current.nextNode


print("Start array:\n", arr_)
addressCalculationSort(arr_)
print("Sorted array:\n", arr_)