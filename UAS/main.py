import os
import model
import view

while True:
    os.system("clear")
    print(f"{'PROGRAM NILAI MAHASISWA':^70}")
    print("="*70)
    print("Silahkan pilih menu :")
    i = input("(T)ambah | (U)bah | (H)apus | (C)ari | (L)ihat | (K)eluar : ")

    #Tambah data
    if i.lower() == 't':
        view.input_nilai.inputUser()
        view.view_nilai.is_done()
    
    #Ubah data
    elif i.lower() == 'u':
        model.daftar_nilai.ubah_data()
        view.view_nilai.is_done()

    #Hapus Data
    elif i.lower() == 'h':
        model.daftar_nilai.hapus_data()
        view.view_nilai.is_done()

    #Cari Data
    elif i.lower() == 'c':
        model.daftar_nilai.cari_data()
        view.view_nilai.is_done()
    
    #Lihat Data
    elif i.lower() == 'l':
       view.view_nilai.lihat_data()
       view.view_nilai.is_done()
       
    #Keluar
    if i.lower() == 'k':
        break

    # else:
    #     print("Silahkan pilih menu yang tersedia!!!")
    #     is_done()
