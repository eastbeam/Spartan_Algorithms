class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def get_kth_node_from_last(self, k):
        cur = self.head
        count = 0
        node_record = []
        while cur.next is not None:
            cur = cur.next
            node_record.append(self.get_node(count).data)
            count += 1
        return node_record[count-k+1]


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
# print(linked_list.get_node(4).data)

print(linked_list.get_kth_node_from_last(2))  # 8이 나와야 합니다!