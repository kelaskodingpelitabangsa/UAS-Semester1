import model
import os

def is_done():
    x = input("Tekan tombol enter untuk melanjutkan!!! ")

def lihat_data():
    os.system("clear")
    print("-"*70)
    print(f"{'PROGRAM NILAI MAHASISWA':^70}")
    print("-"*70)
    print(f"|{'DAFTAR MAHASISWA':^68}|")
    print("-"*70)
    print(f"|{'No':^4}|{'Nama':^15}|{'NIM':^10}|{'Tugas':^7}|{'UTS':^7}|{'UAS':^7}|{'Nilai Akhir':^12}|")
    print("="*70)

    model.daftar_nilai.data()

