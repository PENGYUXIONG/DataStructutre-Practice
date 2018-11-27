class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Doublelinkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        cur_node = self.head

        while cur_node.next is not None:
            cur_node = cur_node.next
        new_node.prev = cur_node
        cur_node.next = new_node
        return

    def display(self):
        display_list = []
        cur_node = self.head
        while cur_node is not None:
            display_list.append(cur_node.data)
            cur_node = cur_node.next
        print(display_list)
        return

    def delete(self, data):
        if self.head is None:
            print('this is an empty list')
            return

        cur_node = self.head

        while cur_node.data != data:
            cur_node = cur_node.next
            if cur_node is None:
                print('no such node exist!')
                return
        prev_node = cur_node.prev
        next_node = cur_node.next

        if prev_node is None and next_node is None:
            self.head = None
            return

        if prev_node is None:
            self.head = cur_node.next
            self.head.prev = None
            return

        if next_node is None:
            prev_node.next = None
            return
        prev_node.next = next_node
        next_node.prev = prev_node
        return

    def reverse(self):
        prev_node = None
        cur_node = self.head
        while cur_node is not None:
            prev_node = cur_node.prev
            cur_node.prev = cur_node.next
            cur_node.next = prev_node
            cur_node = cur_node.prev

        if prev_node is not None:
            self.head = prev_node.prev


sample_list = Doublelinkedlist()
sample_list.append(1)
sample_list.append(2)
sample_list.append(3)
sample_list.append(4)
sample_list.reverse()
sample_list.display()
