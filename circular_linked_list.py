class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class circular_linked_list:
    def __init__(self):
        self.head = None

    def add_at_begining(self, data):
        new_node = Node(data)
        cur_node = self.head

        # if it is an empty list, the new node is going to point to itself
        if self.head is None:
            new_node.next = new_node
        # traverse the linked list, and set the tail point to the head
        else:
            while cur_node.next is not self.head:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        cur_node = self.head

        # if empty list set the head node
        if cur_node is None:
            self.head = new_node
        # traverse and plug in the corresponding node
        else:
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = new_node
        new_node.next = self.head

    def display(self):
        temp_array = []
        cur_node = self.head
        # if it is empty
        if self.head is None:
            print("it is an empty list: " + str(temp_array))
            return
        # if there is only head node
        if self.head.next is self.head:
            temp_array.append(self.head.data)
            print(temp_array)
            return
        # transfer the node list into an array
        while cur_node.next is not self.head:
            temp_array.append(cur_node.data)
            cur_node = cur_node.next
        temp_array.append(cur_node.data)
        print (temp_array)

    def split(self, split_point):
        first_list = circular_linked_list()
        second_list = circular_linked_list()
        # set current node
        cur_node = self.head
        # add the nodes before the split point into the first list
        if cur_node.data == split_point:
            first_list.append(cur_node.data)
            cur_node = cur_node.next
        else:
            while cur_node.data != split_point:
                first_list.append(cur_node.data);
                cur_node = cur_node.next
        # add the nodes equal and after the split point to the second list
        if cur_node.next == self.head:
            second_list.append(cur_node.data)
        else:
            while cur_node is not self.head:
                second_list.append(cur_node.data)
                cur_node = cur_node.next
        return first_list, second_list

    def sorted_insert(self, data):
        new_node = Node(data)

        # start from the head node
        cur_node = self.head

        # if it is an empty list
        if cur_node is None:
            self.head = new_node
            new_node.next = new_node
            return

        # if there is only one element inside
        if cur_node.next == cur_node:
            cur_node.next = new_node
            new_node.next = cur_node
            if cur_node.data > data:
                self.head = new_node
            return

        # if the new node is the smallest
        if cur_node.data > data:
            self.add_at_begining(data)
            return

        # traverse through the whole list to find the appropriate value
        while cur_node.next.data < data:
            if cur_node.next == self.head:
                cur_node.next = new_node
                new_node.next = self.head
                return
            cur_node = cur_node.next

        new_node.next = cur_node.next
        cur_node.next = new_node
        return

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

    def concentrate(self, first_list, second_list):
        # if first list is not empty, keep choosing its head node
        if first_list.head is not None:
            self.head = first_list.head
            # second node is empty means we can return the first_list right away
            if second_list.head is None:
                return

        # lists are empty, it is empty list.......
        elif second_list.head is None:
            print('Two empty Linked list?')
            return

        elif second_list.head is not None:
            self.head = second_list.head
            return

        if self.head is None:
            print('unexpected error!')
            return

        cur_node = self.head

        while cur_node.next is not self.head:
            cur_node = cur_node.next

        cur_node.next = second_list.head
        cur_node = cur_node.next

        while cur_node.next is not second_list.head:
            cur_node = cur_node.next

        cur_node.next = self.head

        return

    def merge_sort(self):
        if self.head is None:
            print('empty node list')
            return

        if self.head.next == self.head:
            print('this is a single node list')
            return self.head

        # check the middle node inside the list
        mid = self.get_middle()
        # split the list into two pieces
        low_list = circular_linked_list()
        high_list = circular_linked_list()

        low_node = self.head
        high_node = mid.next

        low_list.head = low_node
        high_list.head = high_node

        # make the low_list circular node list
        mid.next = low_node

        cur_node = high_node
        while cur_node.next is not low_node:
            cur_node = cur_node.next
        cur_node.next = high_node

        # recursive split
        new_low_node = low_list.merge_sort()
        new_high_node = high_list.merge_sort()

        result_node = self.merge(new_low_node, new_high_node)
        self.head = result_node
        # print(result_node.data)
        return result_node

    def get_middle(self):
        if self.head is None:
            print('there is no node in the list');
            return
        slow = self.head
        fast = self.head
        while fast.next is not self.head and fast.next.next is not self.head:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, low_node, high_node):
        head_node = Node(None)
        cur_node = head_node
        low_head = low_node
        high_head = high_node
        low_start = Node(None)
        high_start = Node(None)

        while low_node is not low_start.next and high_node is not high_start.next:
            if low_node.data < high_node.data:
                cur_node.next = low_node
                low_start.next = low_head
                print(low_node.data)
                cur_node = cur_node.next
                low_node = low_node.next
            else:
                cur_node.next = high_node
                high_start.next = high_head
                print(high_node.data)
                cur_node = cur_node.next
                high_node = high_node.next

        if cur_node.next is not low_head:
            cur_node.next = low_node
            while low_node.next is not low_head:
                low_node = low_node.next
            low_node.next = head_node.next

        elif cur_node.next is not high_head:
            cur_node.next = high_node
            while high_node.next is not high_head:
                high_node = high_node.next
            high_node.next = head_node.next
        return head_node.next


# sample_list = circular_linked_list()
# sample_list.add_at_begining(1)
# sample_list.add_at_begining(2)
# sample_list.add_at_begining(3)
# sample_list.add_at_begining(4)
# sample_list.add_at_begining(5)
# first_list, second_list = sample_list.split(3)
# first_list.display()
# second_list.display()
# sample_list.display(

# sample_list = circular_linked_list()
# sample_list.append(1)
# sample_list.append(2)
# sample_list.append(3)
# sample_list.append(4)
# sample_list.append(5)
# sample_list.display()

# sample_list = circular_linked_list()
# sample_list.sorted_insert(2)
# sample_list.sorted_insert(1)
# sample_list.sorted_insert(1.5)
# sample_list.sorted_insert(-1)
# sample_list.sorted_insert(0)
# sample_list.display()
# print(sample_list.check_circular())


# first_list = circular_linked_list()
# second_list = circular_linked_list()
# sample_list = circular_linked_list()
# first_list.append(1)
# first_list.append(3)
# first_list.append(5)
# second_list.append(2)
# second_list.append(4)
# second_list.append(6)
#
# sample_list.concentrate(first_list, second_list)
# sample_list.display()i

sample_list = circular_linked_list()
sample_list.append(1)
sample_list.append(-2)
sample_list.append(3)
sample_list.append(5)
sample_list.merge_sort()
sample_list.display()
