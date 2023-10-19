from requests import delete

class NodeTabungan:
    no_rek = None
    nama = None
    saldo = None
    next = None
    size = 0

    def __init__(self, no_rek, nama, saldo=0):
        self.no_rek = no_rek
        self.nama = nama
        self.saldo = saldo
        self.next = None
        self.size = 0

class node:
    size = 0
    head = None
    tail = None

    def isEmpty(self):
        return self.size == 0
    
    def len(self):
        return self.size
    
    def insert_head(self, no_rek, nama, saldo):
        new_node = NodeTabungan(no_rek, nama, saldo)

        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            self.tail.next = None

        else:
            new_node.next = self.head
            self.head = new_node
        self.size =+ 1
        print("Data masuk head!")
    
    def delete(self,position):
        if self.isEmpty:
            return False
        elif position == 0:
            self.delete_head()
        elif position + 1 >= self.size:
            self.delete_tail()
        else:
            delete_node = self.head
            for i in range(position):
                delete_node = delete_node.next
                helper = self.head
                while helper.next != delete_node:
                    helper = helper.next
                helper.next = delete_node.next
                del delete_node
                self.size = self.size - 1
    
    def print(self):
        if not self.isEmpty():
            bantu = self.head
            while bantu != None:
                print("Norek : {}".format(bantu.no_rek))
                print("Nama  : {}".format(bantu.nama))
                print("Saldo : {}".format(bantu.saldo))
                bantu = bantu.next
                print()
        else:
            print("Kosong mass ")

    def filter(self,jml):
        self.filter = jml
        bantu = self.head
        count = 0
        while bantu != None:
            if bantu.saldo < self.filter:
                NodeTabungan.delete(bantu)
                count =+ 1
            else:
                bantu = bantu.next
        print("Rekening yang berhasil di hapus sebanyak : {}".format(count))
        print()

    def update(self,jml):
        bantu = self.head
        if jml > 100 or jml < 0 :
            print("Maaf besaran persen harus diantara 0 - 100")
        else:
            while bantu != None:
                saldo = int(bantu.saldo + (bantu.saldo /100 * jml))
                bantu.saldo = saldo
                bantu = bantu.next
            print("Semua saldo rekening berhasil ditambah sebanyak {}%".format(jml))



slnc=node()
slnc.insert_head(201,"Hanif", 250000)
slnc.insert_head(110,"Yudha", 150000)
slnc.print()
slnc.filter(100)
slnc.print()
slnc.update(200)
slnc.update(50)
slnc.print()