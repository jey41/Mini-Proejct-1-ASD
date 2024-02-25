import os
import json
from prettytable import PrettyTable

os.system('cls')

class TokoMebel:
    def __init__(self, nama_toko):
        self.nama_toko = nama_toko
        self.daftar_produk = []
        self.daftar_produk_json = {}
        self.load_data()

    def load_data(self):
        try:
            with open('produk.json', mode='r') as file:
                self.daftar_produk_json = json.load(file)
                for produk in self.daftar_produk_json.values():
                    self.daftar_produk.append(produk)
        except FileNotFoundError:
            # Buat file JSON kosong jika belum ada
            open('produk.json', 'w').close()

    def save_data(self):
        with open('produk.json', mode='w') as file:
            json.dump(self.daftar_produk_json, file, indent=4)

    def add_produk(self, nama_produk, deskripsi, harga, stok, jenis_bahan):
        detail_produk = {"nama_produk": nama_produk, "deskripsi": deskripsi, "harga": harga, "stok": stok, "jenis_bahan": jenis_bahan}
        self.daftar_produk.append(detail_produk)
        self.daftar_produk_json[nama_produk] = detail_produk
        self.simpan_ke_json()
        self.show_produk()

    def show_produk(self):
        table = PrettyTable(["Nama Produk", "Deskripsi", "Harga", "Stok", "Jenis Bahan"])
        for produk in self.daftar_produk:
            table.add_row([produk["nama_produk"], produk["deskripsi"], f"Rp{produk['harga']}", produk["stok"], produk["jenis_bahan"]])

        print(table)

    def update_produk(self, nama_produk, deskripsi=None, harga=None, stok=None, jenis_bahan=None):
        for produk in self.daftar_produk:
            if produk["nama_produk"] == nama_produk:
                if deskripsi is not None:
                    produk["deskripsi"] = deskripsi
                if harga is not None:
                    produk["harga"] = harga
                if stok is not None:
                    produk["stok"] = stok
                if jenis_bahan is not None:
                    produk["jenis_bahan"] = jenis_bahan
        self.daftar_produk_json[nama_produk] = produk
        self.simpan_ke_json()
        self.show_produk()

    def delete_produk(self, nama_produk):
        del self.daftar_produk_json[nama_produk]
        self.daftar_produk = [produk for produk in self.daftar_produk if produk["nama_produk"] != nama_produk]
        self.simpan_ke_json()
        self.show_produk()

    def simpan_ke_json(self):
        with open('produk.json', mode='w') as file:
            json.dump(self.daftar_produk_json, file, indent=4)

toko = TokoMebel("Mebel Jaya Abadi")

while True:
    print("=" * 35)
    print("           Halo admin        ")
    print(f"Selamat datang di {toko.nama_toko}")
    print("=" * 35)
    print("Menu:")
    print("1. Tambah Produk")
    print("2. Tampilkan Produk")
    print("3. Perbarui Produk")
    print("4. Hapus Produk")
    print("5. Keluar")

    try:
        pilihan = int(input("[] Masukkan pilihan Anda (1-5): "))

        if pilihan == 1:
            toko.show_produk()
            nama_produk = input("\n[] Masukkan nama produk: ")
            deskripsi = input("[] Masukkan deskripsi produk: ")
            harga = int(input("[] Masukkan harga produk: "))
            stok = int(input("[] Masukkan stok produk: "))
            jenis_bahan = input("[] Masukkan jenis bahan produk: ")

            print("> Produk berhasil ditambahkan")
            toko.add_produk(nama_produk, deskripsi, harga, stok, jenis_bahan)

        elif pilihan == 2:
            toko.show_produk()

        elif pilihan == 3:
            toko.show_produk()
            nama_produk = input("\n[] Masukkan nama produk yang ingin diperbarui: ")
            deskripsi = input("[] Masukkan deskripsi baru: ")
            harga = int(input("[] Masukkan harga baru: "))
            stok = int(input("[] Masukkan stok baru: "))
            jenis_bahan = input("[] Masukkan jenis bahan baru: ")

            print("> Produk berhasil diperbarui")
            toko.update_produk(nama_produk, deskripsi, harga, stok, jenis_bahan)

        elif pilihan == 4:
            toko.show_produk()
            nama_produk = input("\n[] Masukkan nama produk yang ingin dihapus: ")

            print("> Produk berhasil dihapus")
            toko.delete_produk(nama_produk)

        elif pilihan == 5:
            print("> Terima kasih telah menggunakan program ini!")
            break

        else:
            print("\n> MASUKAN ANGKA YANG TEPAT (1-5)!\n")

    except (ValueError, KeyboardInterrupt, EOFError):
        print("\n> MASUKAN ANGKA!\n")
        break
