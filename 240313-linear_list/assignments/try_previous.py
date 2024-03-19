class Node:
    def __init__(self, data=None):
        self.data = data
        self.pointer = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        print_val = self.head
        while print_val is not None:
            print(print_val.data)
            print_val = print_val.pointer

    def at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.pointer = self.head
        self.head = new_node

    def at_end(self, new_data):
        new_node = Node(new_data)
        laste = self.head
        while (laste.pointer != None):
            laste = laste.pointer
        laste.pointer = new_node

    def in_between(self, middle_node, new_data):
        new_node = Node(new_data)
        new_node.pointer = middle_node.pointer
        middle_node.pointer = new_node

    def remove_node(self, remove_key):
        head_val = self.head
        if (head_val is not None):
            if (head_val.data == remove_key):
                self.head = head_val.pointer
                head_val = None
                return
        while (head_val is not None):
            if head_val.data == remove_key:
                break
            prev = head_val
            head_val = head_val.pointer
        if (head_val == None):
            return
        prev.pointer = head_val.pointer
        head_val = None

# Membuat instance LinkedList
ll = LinkedList()

# Menambahkan node baru di awal
print('Menambah angka 2 di awal list')
ll.at_beginning(2)
ll.print_linked_list()

# Menambahkan node baru di akhir
print('\nmenambahkan angka 8 diakhir list')
ll.at_end(8)
ll.print_linked_list()

# Menambahkan node baru setelah node tertentu
print('\nMenambahkan angka 4 setelah 2')
ll.in_between(ll.head, 4)
ll.print_linked_list()

# Menghapus node dengan nilai tertentu
print('\nMenghapus angka 4')
ll.remove_node(4)
ll.print_linked_list()

print("\nProgram Completed!\n\n--- By L200220277 ---")