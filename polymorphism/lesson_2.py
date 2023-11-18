class Node:
    def __init__(self, value, node=None):
        self.next = node
        self.value = value

    def get_next(self):
        return self.next

    def get_value(self):
        return self.value

    def __repr__(self):
        acc = []
        current = self
        while current is not None:
            acc.append(current.get_value())
            current = current.get_next()
        return str(tuple(acc))


def reverse(data):
    reversed_list = None
    current = data

    while current:
        reversed_list = Node(current.get_value(), reversed_list)
        current = current.get_next()

    return reversed_list



numbers = Node(1, Node(2, Node(3)))  ## (1, 2, 3)
print(reverse(numbers))
# reversed_numbers = reverse(numbers)  ## (3, 2, 1)
