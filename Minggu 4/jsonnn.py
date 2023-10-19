import json
# data = dict()

# n1 = input("Masukkan jumlah mahasiswa baru : ")

# for i in range(n1):
#     nama_mhs = input("Masukkan nama Anda : ")
#     n3 = input("Masukkan Jumlah Hobi : ")
#     for j in range(n3):
#         n4 = input("Masukkan Hobi ke-",len(n3),": ")
#     n5 = input("Masukkan Prestasi anda : ")

# with open("mahasiswa.json","w",) as datafile:
#     json.dump(data, datafile)
data_new = None
with open("mahasiswa.json", "r") as datafile:
    data_new = json.load(datafile)

    jml_mhs = int(input("Masukkan jumlah mahasiswa baru : "))

for i in range(jml_mhs):
    nama_mhs = input("Masukkan nama Anda : ")
    hobi_mhs = int(input("Masukkan Jumlah Hobi : "))
    list_hobi = []
    for i in range(1,hobi_mhs + 1):
        bnyk_hobi = input("Masukkan Hobi ke-")
        list_hobi.append(bnyk_hobi)
    n5 = input("Masukkan Prestasi anda : ")

    data_new['BioData', 'Prestasi'] = list_hobi,n5
    
with open ("mahasiswa.json", "w") as datafile:
    json.dump(data_new, datafile)
    data_new.close()



