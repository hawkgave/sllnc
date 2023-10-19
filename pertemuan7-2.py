from SLLNC import SLLNC

class Stack:
    def __init__(self):
        self.data = SLLNC()

    def __len__(self):
        return len(self.data)
    
    def IsEmpty(self):
        return len(self.data) == 0
    
    def push(self, data_baru):
        self.data.addElementTail(data_baru)

    def pop(self): #untuk mengeluarkan data yang paling terakhir
        if self.IsEmpty():
            print('Stack is Empty!')
        hapus = self.data._tail
        self.data.deleteLast()
        return hapus._elemental

    def top(self): #melihat data terakhir yang dimasukkan -- peek
        if self.IsEmpty():
            print('Stack Is Empty')
        return self.data._tail._element
    
    def printAll(self):
        helper = self.data._head
        print('Data: ', end='')
        while helper != None:
            print(helper._element, end='')
            helper = helper._next
        print()

if __name__ == '__main__':
    st = Stack()
    st.push ('Aga')
    st.push ('Yohanes')
    st.push ('Thanel')
    st.push ('Rendy')
    st.push ('Ave')
    st.push ('Yosua')
    st.push ('Cynthia')
    st.push ('Yeheskiel')
    st.pop()
    st.pop()
    st.pop()
    st.top()
    st.pop()
    st.printAll()
    print('Panjang Data: ', len(st))