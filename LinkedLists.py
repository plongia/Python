class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:


    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def add_node(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def remove_node(self, search_data):
        previous_node = None
        current_node = self.head
        data_found = False
        while current_node is not None and data_found is False:
            if self.head is None:
                print("List is empty")
                break
            if current_node.get_data() == search_data:
                if current_node == self.head:
                    self.head = current_node.get_next()
                    data_found = True
                else:
                    previous_node.set_next(current_node.get_next())
                    data_found = True
            else:
                previous_node = current_node
                current_node = current_node.get_next()

    def search(self, search_data):
        previous_node = None
        current_node = self.head
        data_found = False
        while current_node is not None and not data_found:
            if current_node.get_data() == search_data:
                print("Data Found")
                data_found = True
            else:
                previous_node = current_node
                current_node = current_node.get_next()
        return data_found

    def length(self):
        length = 0
        current_node = self.head
        while current_node is not None:
            length = length + 1
            current_node = current_node.get_next()
        return length

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.get_data())
            current_node = current_node.get_next()

    def print_sorted_list(self):
        sorted_list = []
        current_node = self.head
        while current_node is not None:
            sorted_list.append(current_node.get_data())
            current_node = current_node.get_next()
        sorted_list.sort()
        return sorted_list


ll = LinkedList()
print(f"length: {ll.length()}")
ll.add_node("Cat")
ll.add_node("Dog")
print(f"length: {ll.length()}")
print(f"Dog Exists: {ll.search('Dog')}")
print(f"Bird Exists: {ll.search('Bird')}")
ll.remove_node("Cat")
print(f"length: {ll.length()}")
ll.add_node("Dad")
ll.add_node("Vivan")
ll.print_list()
print(f"Sorted List: {ll.print_sorted_list()}")
