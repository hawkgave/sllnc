from mobil import mobil

mobil1 = mobil("toyota", "avanza")
mobil1.print_info()

mobil2 = mobil("nissan", "grand livina")
mobil2.set_bahan_bakar("minyak goreng")
mobil2.set_kapasBBM(20)
mobil2.print_info()

mobil1.isi_bbm(14500)
mobil2.isi_bbm(14500)