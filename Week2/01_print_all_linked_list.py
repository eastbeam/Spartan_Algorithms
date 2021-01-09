class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node = Node(3)
first_node = Node(4)
node.next = first_node

print(node.data)
print(first_node.data)
print(node.next)


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)
        # print(cur)

    def print_all(self):
        print('hihihi')
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


linked_list = LinkedList(3)
print(linked_list)
print(linked_list.head)
print(linked_list.head.data)
linked_list.append(7)
linked_list.append(4)
linked_list.print_all()