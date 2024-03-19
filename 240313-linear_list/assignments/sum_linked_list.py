class Node:
    def __init__(self, data=None):
        # Inisialisasi node dengan data yang diberikan
        self.data = data
        # Pointer untuk menunjuk ke node berikutnya, awalnya diatur None
        self.pointer = None

class LinkedList:
    def __init__(self):
        # Inisialisasi linked list dengan kepala (head) yang awalnya None
        self.head = None

    def print_linked_list(self):
        # Mencetak semua data dalam linked list
        print_val = self.head
        while print_val is not None:
            print(print_val.data)
            print_val = print_val.pointer

    def at_beginning(self, new_data):
        # Menambahkan node baru di awal linked list
        new_node = Node(new_data)
        new_node.pointer = self.head
        self.head = new_node

    def at_end(self, new_data):
        # Menambahkan node baru di akhir linked list
        new_node = Node(new_data)
        # Jika linked list kosong, node baru akan menjadi kepala
        if self.head is None:
            self.head = new_node
            return
        # Jika tidak, mencari node terakhir dan menambahkan node baru di belakangnya
        laste = self.head
        while laste.pointer is not None:
            laste = laste.pointer
        laste.pointer = new_node

    def in_between(self, middle_node, new_data):
        # Menambahkan node baru setelah node tertentu
        if middle_node is None:
            print("Node referensi tidak ada")
            return
        new_node = Node(new_data)
        new_node.pointer = middle_node.pointer
        middle_node.pointer = new_node

    def remove_node(self, remove_key):
        # Menghapus node dengan nilai tertentu
        head_val = self.head
        # Jika node yang dihapus adalah kepala
        # maka head_val diubah menjadi pointer node selanjutnya
        if head_val is not None and head_val.data == remove_key:
            self.head = head_val.pointer
            head_val = None
            return
        # Mencari node yang akan dihapus
        while head_val is not None:
            if head_val.data == remove_key:
                break
            prev = head_val
            head_val = head_val.pointer
        # Jika node tidak ditemukan
        if head_val is None:
            return
        # Menghapus node dan mengatur pointer node sebelumnya
        prev.pointer = head_val.pointer
        head_val = None

    def sum_linked_list(self):
        # Menghitung jumlah dari semua data dalam linked list
        current = self.head
        total_sum = 0
        while current is not None:
            total_sum += current.data
            current = current.pointer
        # Mengembalikan total jumlah dan cetak jumlahnya
        return total_sum

# Membuat instance linked list
ll = LinkedList()

# Menambahkan 6 node baru di awal
print('Menambah angka 3,5,2,6,9,7 di awal list')
for i in [3,5,2,6,9,7]:
    ll.at_beginning(i)

# Menghitung semua data dalam linked list
print('\nMenghitung semua data')
ll.print_linked_list()
print('Total =', ll.sum_linked_list())

print("\nProgram Completed!\n\n--- By L200220277 ---")