from random import randint


arr_ = [randint(0, 100) for i in range(10)]


class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value


def inorder(root, res):
    if root:
        inorder(root.left, res)
        res.append(root.value)
        inorder(root.right, res)


def tree_sort(arr):
    if len(arr) == 0:
        return arr
    root = node(arr[0])
    for i in range(1, len(arr)):
        root.insert(arr[i])
    res = []
    inorder(root, res)
    return res


if __name__ == "__main__":
    print("Start array:\n", arr_)
    print("Tree sort:\n", tree_sort(arr_))
