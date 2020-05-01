

arr = [i for i in range(10)]
print(arr)


def add_num(a, num, pos):
    tmp = a[pos:]
    a = (a[:pos]) + [num]
    return a + tmp


def replace(a, pos1, pos2):
    tmp = a[pos2]
    a[pos1], a[pos2] = tmp, a[pos1]
    return a


def del_num(a, pos):
    del a[pos]
    return a


print("add element", add_num(arr, 100, 5))
print("replace elements", replace(arr, 1, 5))
print("del element", del_num(arr, 1))


class List:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def add_node_end(self, node, value=None):
        start = node
        while node.next is not None:
            node = node.next
        node.next = List(value)
        return start

    def add_node_pos(self, start, pos, value=None):
        i = 1
        prev = None
        curr = start
        while i < pos:
            prev = curr
            curr = curr.next
            i += 1
        prev.next = List(value)
        prev.next.next = curr
        return start

    def add_node_front(self, start, value=None):
        next = start.next
        start = List(value)
        start.next = next
        return start

    def del_node(self, start, pos):
        i = 1
        prev = None
        curr = start
        while i < pos:
            prev = curr
            curr = curr.next
            i += 1
        if prev is not None:
            prev.next = curr.next
        else:
            start = curr.next
        return start

    def show_list(self, start, text=None):
        print(f"List ({text}):")
        while start.next is not None:
            print(start.value, end=', ')
            start = start.next
        print(start.value)


start = List(0)
for i in range(1, 10):
    start = start.add_node_end(start, i)

start.show_list(start, 'create list with adding node in the end')
start = start.add_node_pos(start, 5, 100)
start.show_list(start, 'add new node')
start = start.add_node_front(start, 100)
start.show_list(start, 'add new node in the start')
start = start.del_node(start, 5)
start.show_list(start, 'del node')


