# class ArrayStack:
#     def __init__(self):
#         self.data = []
    
#     def __len__(self):
#         return len(self.data)
    
#     def IsEmpty(self):
#         return len(self.data) == 0
    
#     def push(self, data): #untuk nambahin data
#         self.data.append(data)

#     def pop(self): #untuk mengeluarkan data yang paling terakhir
#         if self.IsEmpty():
#             print('Stack is Empty!')
#         return self.data.pop()

#     def top(self): #melihat data terakhir yang dimasukkan -- peek
#         if self.IsEmpty():
#             print('Stack Is Empty')
#         return self.data[-1]
    
#     def printAll(self):
#         print ('Data: ', *self.data, sep=' ')
#         # if self.IsEmpty():
#         #     print('Empty')
#         # else:
#         #     return ' '.join(self.data)
#         # for data in self.data:
#         #     print(data, ends='')
    
# if __name__ == '__main__':
#     st = ArrayStack()
#     st.push ('Aga')
#     st.push ('Yohanes')
#     st.push ('Thanel')
#     st.push ('Rendy')
#     st.push ('Ave')
#     st.pop()
#     st.pop()
#     st.push ('Yosua')
#     st.push ('Cynthia')
#     st.pop()
#     st.push ('Yeheskiel')
#     st.top()
#     st.pop()
#     #st.printAll()
#     # print(st.top())
#     # print(st.pop())
#     print('Panjang Data: ', len(st))

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
            
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.top = self.top.next
            self.size -= 1
            return data
        else:
            return None

    def print_stack(self):
        current = self.top
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

# Membuat objek Stack
stack = Stack()

while stack.size < 10:
    try:
        angka = int(input("Masukkan angka: "))
        if angka not in [node.data for node in stack]:
            stack.push(angka)
        else:
            print("Angka sudah ada di dalam Stack.")
        print("Isi Stack: ", end='')
        stack.print_stack()
    except ValueError:
        print("Input tidak valid. Masukkan angka.")

print("Stack telah mencapai batas 10 elemen. Isi Stack akhir: ", end='')
stack.print_stack()


    def push(self,e): 
        baru = Node(e, None)
        if self.isEmpty():
            self._head = baru
            self._tail = baru
            self._tail._next = None
        else:
            baru._next = self._tail
            self._tail= baru
            while baru._next :
                baru = baru._next
        self._size += 1
