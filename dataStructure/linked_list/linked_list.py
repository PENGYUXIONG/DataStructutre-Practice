class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None

    def Isempty(self):
        if self.head is None:
            return True
        return False

    def append(self, new_data):
        new_node = node(new_data)
        if self.Isempty():
            self.head = new_node
            return
        # traverse from the head of the linked list
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = new_node

    def display(self):
        elem = []
        # traverse from the head of the linked list
        cur_node = self.head
        while cur_node is not None:
            elem.append(cur_node.data)
            cur_node = cur_node.next
        print(elem)

    def length(self):
        length = 0
        # traverse from the head of the linked list
        cur_ndoe = self.head
        while cur_ndoe is not None:
            cur_ndoe = cur_ndoe.next
            length = length + 1
        return length

    def insert(self, prev_value, value):
        new_node = node(value)
        # traverse from the head of the linked list
        cur_node = self.head
        if self.Isempty():
            self.head = new_node
            return
        while cur_node.data != prev_value:
            cur_node = cur_node.next
        # record the next node
        next_node = cur_node.next
        cur_node.next = new_node
        new_node.next = next_node

    def add_new_begin(self, value):
        # set new head
        second_node = self.head
        self.head = node(value)
        self.head.next = second_node

    def remove_by_value(self, value):
        if self.Isempty():
            print("the linked_list is empty")
            return
        # traverse from the head of the linked list
        cur_node = self.head
        # in case remove the first node
        if cur_node.data == value:
            self.head = self.head.next
            return
        while cur_node.next.data != value:
            cur_node = cur_node.next
        cur_node.next = cur_node.next.next

    def remove_by_pos(self, pos):
        if self.Isempty():
            print("the linked_list is empty")
            return

        # in case want to remove the first node aka head
        if pos == 0:
            self.head = self.head.next
            return

        # in case the position exceeds the limit
        if pos > self.length():
            print("the index exceeds the range of this linked list")
            return

        # traverse from the head of the linked list
        cur_node = self.head
        for i in range(pos-1):
            cur_node = cur_node.next
        cur_node.next = cur_node.next.next

    def reverse(self):
        if self.Isempty():
            print("this is an empty linked list")
            return
        # set the start node
        cur_node = self.head
        # set the tail.next
        prev_node = None
        # go over the linked list
        while cur_node is not None:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        # set the head to be the last node
        self.head = prev_node

    def get_tail(self):
        # make sure the node_list is not empty
        if self.Isempty():
            print("this is an empty linked list")
            return
        # set the current node to start from the first node
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        return cur_node

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

    def check_circular(self):
        cur_node = self.head

        # in case the list is empty
        if self.head is None:
            return True

        while cur_node is not None and cur_node.next != self.head:
            cur_node = cur_node.next

        # if there is an end for the linked_list
        if cur_node is None:
            return False
        else:
            return True

    def insert_in_order(self, data):
        cur_node = self.head
        new_node = node(data)

        if cur_node is None:
            self.head = new_node
            return

        if data < cur_node.data:
            self.head = new_node
            new_node.next = cur_node
            return

        while cur_node is not None:

            if cur_node.next is None:
                cur_node.next = new_node
                return

            if cur_node.next.data < data:

                cur_node = cur_node.next
                continue

            new_node.next = cur_node.next
            cur_node.next = new_node
            return

    def merge_sort(self):
        if self.head is None:
            print('this is an empty node list')
            return

        if self.head.next is None:
            print('only one node, no need to get merge sort working')
            return self.head

        # init two linked lists to assign two halves of the list
        low_list = linked_list()
        high_list = linked_list()

        mid = self.get_middle()
        cur_node = self.head

        low_list.head = self.head
        high_list.head = mid

        while cur_node.next is not mid:
            cur_node = cur_node.next
        cur_node.next = None

        low_node = low_list.merge_sort()
        high_node = high_list.merge_sort()

        self.head = self.merge(low_node, high_node)
        return self.head

    def get_middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, low_node, high_node):
        head_node = node(None)
        cur_node = head_node

        cur_low_node = low_node
        cur_high_node = high_node

        while cur_low_node is not None and cur_high_node is not None:
            if cur_low_node.data < cur_high_node.data:
                cur_node.next = cur_low_node
                cur_node = cur_node.next
                cur_low_node = cur_low_node.next
            else:
                cur_node.next = cur_high_node
                cur_node = cur_node.next
                cur_high_node = cur_high_node.next

        if cur_low_node is not None:
            cur_node.next = cur_low_node

        elif cur_high_node is not None:
            cur_node.next = cur_high_node

        return head_node.next


sample_list = linked_list()
# sample_list.append(0)
# sample_list.append(2)
# sample_list.insert(0, 3)
# sample_list.remove_by_value(0)
# sample_list.add_new_begin(9)
# sample_list.remove_by_pos(2)
# sample_list.reverse()
#
#
# sample_list.append(10)
# sample_list.append(0)
# sample_list.append(5)
# sample_list.append(4)
# sample_list.append(7)
# sample_list.append(20)
# sample_list.append(0)
# sample_list.quick_sort()
# sample_list.display()
# print(sample_list.check_circular())


# sample_list = linked_list()
# sample_list.insert_in_order(5)
# sample_list.insert_in_order(1)
# sample_list.insert_in_order(-1)
# sample_list.insert_in_order(20)
# sample_list.display()

sample_list = linked_list()
sample_list.append(1)
sample_list.append(-2)
sample_list.append(3)
sample_list.append(5)
sample_list.append(13)
sample_list.display()
sample_list.merge_sort()
sample_list.display()
