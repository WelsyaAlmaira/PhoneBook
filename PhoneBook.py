"""
Nama    : Welsya Almaira Indra
NIM     : 221524032
Kelas   : 1A - TI4
Tanggal : 17-02-2023

"""
# FUNCTION
# Menampilkan isi dari file txt phonebook
def lihatFile():
    file = open("phonebook.txt", "r") # Buka file text
    isi = file.read() # Baca isi file
    file.close() # Tutup file
    if len(isi) == 0:
        print("Phone Book kosong")
    else:
        print(isi)

# Menambahkan kontak ke phonebook
def insertKontak(nama, nomor):
    file = open("phonebook.txt", "a")
    file.write(nama + " " + nomor + "\n")
    file.close()
    print("=== Kontak telah ditambahkan ===")

# Mencari kontak di phonebook
def searchKontak() :
    cari = input("\nNama kontak yang ingin dicari : ")
    with open("phonebook.txt", 'r') as file:
        for isi in file:
            if cari in isi:
                print("Ini adalah kontak yang Anda cari : \n", isi)
                return
    print("\n-- Kontak yang Anda cari tidak ada --")
    file.close()

# Menghapus kontak dari phonebook
def deleteKontak() :
    kontak = input("\nNama kontak yang ingin dihapus : ")
    file = open("phonebook.txt","r")
    simpan = {}
    i = 0
    isi = file.readline()
    temp = isi.split(" ")
    while isi:
        if temp[0] == kontak:
            del(isi)
        else:
            simpan[i] = isi
            i += 1
        isi = file.readline()
        temp = isi.split(" ")
    file.close
    file = open("phonebook.txt","w")
    for nama in simpan:
        file.write(simpan[nama])
    print(kontak, "telah dihapus dari Phone Book")

# Meng-update kontak di phonebook
def updateKontak() :
    with open("phonebook.txt", "r") as file:
        isi = file.read()
    print("Mau update nomor atau nama kontak?")
    print("1. Nomor")
    print("2. Nama")
    pilih = input("Pilih : ")
    if int(pilih) == 1:
        noLama = input("Input nomor lama : ")
        noBaru = input("Input nomor baru : ")
        isiBaru = isi.replace(noLama, noBaru)
        with open("phonebook.txt", "a") as file:
            file.write(isiBaru)
        print("Berhasil di-update!")
    elif int(pilih) == 2:
        namaLama = input("Nama sebelumnya : ")
        namaBaru = input("Nama baru : ")
        isiBaru = isi.replace(namaLama, namaBaru)
        with open("phonebook.txt", "w") as file:
            file.write(isiBaru)
        print("Berhasil di-update!")
    else :
        print("\nPilihan Anda tidak valid, coba lagi")


# PROGRAM UTAMA
print("+------------------------------------+")
print("|         PROGRAM PHONE BOOK         |")
print("+------------------------------------+")

while True:
    print("\n======================================")
    print("1. Lihat Phone Book")
    print("2. Insert Kontak")
    print("3. Cari Kontak")
    print("4. Hapus Kontak")
    print("5. Update Kontak")
    print("0. Keluar")
    menu = input("Pilih Menu : ")
    print("======================================")

    if int(menu) == 1:
        print("\n============= PHONE BOOK =============\n")
        lihatFile()  
    elif int(menu) == 2:
        nama = input("\nMasukkan nama kontak : ")
        nomor = input("Masukkan nomor : ")
        insertKontak(nama, nomor)
    elif int(menu) == 3:
        searchKontak()
    elif int(menu) == 4:
        deleteKontak()
    elif int(menu) == 5:
        updateKontak()
    elif int(menu) == 0:
        print("\n=== Terima kasih telah menggunakan program ini! ===")
        break
    else :
        print("\nPilihan Anda tidak valid, coba lagi")