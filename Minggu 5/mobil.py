class mobil:
    _merk = ""
    _tipe = ""
    _bahan_bakar = ""
    _kapas_bbm = 0

    def __init__(self, _merk, _tipe):
        self._merk = _merk
        self._tipe = _tipe
        self._bahan_bakar = None
        self._kapas_bbm = None

    def set_merk(self, _merk):
        self._merk = _merk

    def set_tipe(self, _tipe):
        self._tipe = _tipe

    def set_kapasBBM(self,_kapas_bbm):
        self._kapas_bbm = _kapas_bbm

    def set_bahan_bakar(self,_bahan_bakar):
        self._bahan_bakar = _bahan_bakar

    def print_info(self):
        print("========== INFO ==========")
        print("Merk             : ", self._merk)
        print("Tipe             : ", self._tipe)
        print("Bahan Bakar      : ", self._bahan_bakar)
        print("Kapasitas BBM    : ", self._kapas_bbm)
    
    def isi_bbm(self,_harga):
        print("Mengisi ")
        if self._bahan_bakar == None or self._kapas_bbm == None:
            print("ERROR!! Baikin inputan, nnti dimarahin kak Shaloom dan kak Beatrix")
        
        else :
            print("Total Harga : RP"+ str(_harga * self._kapas_bbm))