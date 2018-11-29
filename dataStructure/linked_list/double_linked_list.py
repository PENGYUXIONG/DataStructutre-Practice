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
        return

    def quick_sort(self):
        if self.head is None:
            print("This is an empty node list")
            return
        # set the head of the node list to be the start node
        init_low_node = self.head
        # get the tail node
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        init_high_node = cur_node

        # make sure that the node does exist
        def partition(low_node, high_node):
            if low_node == high_node:
                return
            # set the pivot node to start from the low node
            pivot_node = low_node
            # check from the next node
            cur_node = pivot_node.next
            while cur_node is not high_node:
                if cur_node.data < pivot_node.data:
                    # swap pivot node's next node's data with the smaller node
                    temp = pivot_node.next
                    temp.data, cur_node.data = cur_node.data, temp.data
                    pivot_node.data, temp.data = temp.data, pivot_node.data

                    pivot_node = pivot_node.next

                cur_node = cur_node.next
            partition(low_node, pivot_node)
            partition(pivot_node.next, high_node)

        partition(init_low_node, init_high_node.next)




sample_list = Doublelinkedlist()
sample_list.append(1)
sample_list.append(2)
sample_list.append(3)
sample_list.append(4)
sample_list.reverse()
sample_list.quick_sort()
sample_list.display()
