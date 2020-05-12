class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None





class LinkedList():
    def __init__(self):
        self.head = None
        self.count = 0

    def add_node(self, data):
        new_node = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        self. count += 1

    def find_node(self,i):
        temp = self.head
        for i in range(i):
            temp = temp.next
            return temp.data


    # def add_node(self, data, next):



    # def get_node(selfs, y):
    #     self.linked_list[y]

linked_list = LinkedList()

linked_list.head = Node(6)
linked_list.add_node(1)
linked_list.add_node(5)
linked_list.add_node(3)
