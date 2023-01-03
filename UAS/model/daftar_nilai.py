mahasiswa_template = {
    'nama':'nama',
    'nim':'000000000',
    'uts':0,
    'uas':0,
    'tugas':0,
    'nilai_akhir':0
}

data_mahasiswa = {}

def tambah_data():
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())

    mahasiswa['nama'] = input("Nama           : ")
    mahasiswa['nim'] = int(input("NIM            : "))
    mahasiswa['tugas'] = int(input("Nilai Tugas    : "))
    mahasiswa['uts'] = int(input("Nilai UTS      : "))
    mahasiswa['uas'] = int(input("Nilai UAS      : "))
    mahasiswa['nilai_akhir'] = mahasiswa['tugas']*0.30 + mahasiswa['uts']*0.35 + mahasiswa['uas']*0.35

    KEY = mahasiswa['nim']
    data_mahasiswa.update({KEY:mahasiswa})

    print("-"*70)
    print(f"{'TAMBAH NILAI MAHASISWA':^70}")
    print("-"*70)
    print(f"|{'Nama':^15}|{'NIM':^10}|{'Tugas':^8}|{'UTS':^8}|{'UAS':^8}|{'Nilai Akhir':^14}|")
    print("="*70)
    print(f"|{mahasiswa['nama']:^15}|{mahasiswa['nim']:^10}|{mahasiswa['tugas']:^8}|{mahasiswa['uts']:^8}|{mahasiswa['uas']:^8}|{mahasiswa['nilai_akhir']:^14.2f}|")
    print("-"*70)

def ubah_data():
    print("Silahkan masukkan NIM yang akan di ubah datanya,")
    nim_input = int(input("NIM            : "))
    if nim_input in data_mahasiswa.keys():
        data_mahasiswa[nim_input]['tugas'] = int(input("Nilai Tugas    : "))
        data_mahasiswa[nim_input]['uts'] = int(input("Nilai UTS      : "))
        data_mahasiswa[nim_input]['uas'] = int(input("Nilai UAS      : "))
        data_mahasiswa[nim_input]['nilai_akhir']= data_mahasiswa[nim_input]['tugas']*0.30 + data_mahasiswa[nim_input]['uts']*0.35 + data_mahasiswa[nim_input]['uas']*0.35
        
        print("-"*70)
        print(f"|{'Nama':^15}|{'NIM':^10}|{'Tugas':^8}|{'UTS':^8}|{'UAS':^8}|{'Nilai Akhir':^14}|")
        print("="*70)
        print(f"|{data_mahasiswa[nim_input]['nama']:^15}|{data_mahasiswa[nim_input]['nim']:^10}|{data_mahasiswa[nim_input]['tugas']:^8}|{data_mahasiswa[nim_input]['uts']:^8}|{data_mahasiswa[nim_input]['uas']:^8}|{data_mahasiswa[nim_input]['nilai_akhir']:^14.2f}|")
        print("-"*70)

    else:
        print(f"NIM {nim_input} tidak ditemukan!!!")

def hapus_data():
    print("Silahkan masukkan NIM yang akan di hapus,")
    nim_input = int(input("NIM            : "))
    if nim_input in data_mahasiswa.keys():
        del data_mahasiswa[nim_input]
        print(f"Data NIM {nim_input} berhasil di hapus")

    else:
        print(f"NIM {nim_input} tidak ditemukan!!!")

def cari_data():
    print("Silahkan masukkan NIM yang akan di cari,")
    nim_input = int(input("NIM           : "))
    if nim_input in data_mahasiswa.keys():
        print("-"*70)
        print(f"|{'DAFTAR MAHASISWA':^68}|")
        print("-"*70)
        print(f"|{'Nama':^15}|{'NIM':^10}|{'Tugas':^8}|{'UTS':^8}|{'UAS':^8}|{'Nilai Akhir':^14}|")
        print("="*70)
        print(f"|{data_mahasiswa[nim_input]['nama']:^15}|{data_mahasiswa[nim_input]['nim']:^10}|{data_mahasiswa[nim_input]['tugas']:^8}|{data_mahasiswa[nim_input]['uts']:^8}|{data_mahasiswa[nim_input]['uas']:^8}|{data_mahasiswa[nim_input]['nilai_akhir']:^14.2f}|")
        print("-"*70)

    else:
        print(f"NIM {nim_input} tidak ditemukan!!!")

def data():
    if data_mahasiswa.items():
        no = 1
        for mahasiswa in data_mahasiswa.items():
            print(f"|{no:^4}|{mahasiswa[1]['nama']:^15}|{mahasiswa[1]['nim']:^10}|{mahasiswa[1]['tugas']:^7}|{mahasiswa[1]['uts']:^7}|{mahasiswa[1]['uas']:^7}|{mahasiswa[1]['nilai_akhir']:^12.2f}|")
            no += 1
        print("-"*70)

    else:
        print(f"|{'TIDAK ADA DATA':^68}|")
        print("="*70)