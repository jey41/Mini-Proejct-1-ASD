import os
from prettytable import PrettyTable

os.system('cls')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class TokoMebel:
    def __init__(self, nama_toko):
        self.nama_toko = nama_toko
        self.head = None
        self.tail = None
        
    def add_produk_awal(self, nama_produk, deskripsi, harga, stok, jenis_bahan):
        new_node = Node(
            {
                "nama_produk": nama_produk,
                "deskripsi": deskripsi,
                "harga": harga,
                "stok": stok,
                "jenis_bahan": jenis_bahan,
            }
        )
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        print("> Produk berhasil ditambahkan di awal")

    # Menambahkan node di akhir
    def add_produk_akhir(self, nama_produk, deskripsi, harga, stok, jenis_bahan):
        new_node = Node(
            {
                "nama_produk": nama_produk,
                "deskripsi": deskripsi,
                "harga": harga,
                "stok": stok,
                "jenis_bahan": jenis_bahan,
            }
        )
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            print("> Produk berhasil ditambahkan di akhir")

    # Menambahkan node di tengah
    def add_produk_tengah(self, nama_produk, deskripsi, harga, stok, jenis_bahan, nama_produk_sebelumnya):
        curr_node = self.head
        prev_node = None
        
        while curr_node is not None and curr_node.data["nama_produk"] != nama_produk_sebelumnya:
            prev_node = curr_node
            curr_node = curr_node.next
        
        if curr_node is None:
            print("> Produk tidak ditemukan")
        else:
            new_node = Node(
                {
                  "nama_produk": nama_produk,
                  "deskripsi": deskripsi,
                  "harga": harga,
                  "stok": stok,
                  "jenis_bahan": jenis_bahan,
                }
            )
            if prev_node is None:
                self.head = new_node
            else:
                prev_node.next = new_node
            new_node.next = curr_node
            print("> Produk berhasil ditambahkan di tengah")

    def show_produk(self):
        if self.head is None:
            print("> Data produk kosong")
            return
        table = PrettyTable(["Nama Produk", "Deskripsi", "Harga", "Stok", "Jenis Bahan"])
        curr_node = self.head
        while curr_node is not None:
            produk = curr_node.data
            table.add_row([produk["nama_produk"], produk["deskripsi"], f"Rp{produk['harga']}", produk["stok"], produk["jenis_bahan"]])
            curr_node = curr_node.next
        print(table)

    def update_produk(self, nama_produk, deskripsi, harga, stok, jenis_bahan):
        curr_node = self.head
        while curr_node is not None and curr_node.data["nama_produk"] != nama_produk:
            curr_node = curr_node.next
        if curr_node is None:
            print("> Produk tidak ditemukan")
        else:
            curr_node.data["deskripsi"] = deskripsi
            curr_node.data["harga"] = harga
            curr_node.data["stok"] = stok
            curr_node.data["jenis_bahan"] = jenis_bahan
            print("> Produk berhasil diperbarui")

    def delete_produk_awal(self):
        if self.head is None:
            print("> Data produk kosong")
        else:
            temp = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            del temp
            print("> Produk berhasil dihapus dari awal")

    # Menghapus node di akhir
    def delete_produk_akhir(self):
        if self.head is None:
            print("> Data produk kosong")
        else:
            prev_node = None
            curr_node = self.head
            while curr_node.next is not None:
                prev_node = curr_node
                curr_node = curr_node.next
            if prev_node is None:
                self.head = self.tail = None
            else:
                prev_node.next = None
                self.tail = prev_node
            del curr_node
            print("> Produk berhasil dihapus dari akhir")

    # Menghapus node di tengah
    def delete_produk_tengah(self, nama_produk):
        prev_node = None
        curr_node = self.head
        
        while curr_node is not None and curr_node.data["nama_produk"] != nama_produk:
            prev_node = curr_node
            curr_node = curr_node.next
        
        if curr_node is None:
            print("> Produk tidak ditemukan")
        else:
            if prev_node is None:
                self.head = self.head.next
            else:
                prev_node.next = curr_node.next
            if curr_node == self.tail:
                self.tail = prev_node
            del curr_node
            print("> Produk berhasil dihapus dari tengah")

toko = TokoMebel("Mebel Jaya Abadi")

while True:
    print("=" * 35)
    print("           Halo admin        ")
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
            print("\n1. Tambah di Awal")
            print("2. Tambah di Akhir")
            print("3. Tambah di Tengah")
            pilih_tambah = int(input("[] Masukkan pilihan penambahan (1-3): "))
            
            if pilih_tambah == 1:
                nama_produk = input("\n[] Masukkan nama produk: ")
                deskripsi = input("[] Masukkan deskripsi produk: ")
                harga = int(input("[] Masukkan harga produk: "))
                stok = int(input("[] Masukkan stok produk: "))
                jenis_bahan = input("[] Masukkan jenis bahan produk: ")
                toko.add_produk_awal(nama_produk, deskripsi, harga, stok, jenis_bahan)

            elif pilih_tambah == 2:
                nama_produk = input("\n[] Masukkan nama produk: ")
                deskripsi = input("[] Masukkan deskripsi produk: ")
                harga = int(input("[] Masukkan harga produk: "))
                stok = int(input("[] Masukkan stok produk: "))
                jenis_bahan = input("[] Masukkan jenis bahan produk: ")
                toko.add_produk_akhir(nama_produk, deskripsi, harga, stok, jenis_bahan)

            elif pilih_tambah == 3:
                nama_produk = input("\n[] Masukkan nama produk: ")
                deskripsi = input("[] Masukkan deskripsi produk: ")
                harga = int(input("[] Masukkan harga produk: "))
                stok = int(input("[] Masukkan stok produk: "))
                jenis_bahan = input("[] Masukkan jenis bahan produk: ")
                nama_produk_sebelumnya = input("[] Masukkan nama produk di depannya: ")
                toko.add_produk_tengah(nama_produk, deskripsi, harga, stok, jenis_bahan, nama_produk_sebelumnya)

        elif pilihan == 2:
            toko.show_produk()

        elif pilihan == 3:
            toko.show_produk()
            nama_produk = input("\n[] Masukkan nama produk yang ingin diperbarui: ")
            deskripsi = input("[] Masukkan deskripsi baru: ")
            harga = int(input("[] Masukkan harga baru: "))
            stok = int(input("[] Masukkan stok baru: "))
            jenis_bahan = input("[] Masukkan jenis bahan baru: ")

            toko.update_produk(nama_produk, deskripsi, harga, stok, jenis_bahan)

        elif pilihan == 4:
            toko.show_produk()
            print("\n1. Hapus di Awal")
            print("2. Hapus di Akhir")
            print("3. Hapus di Tengah")
            pilih_hapus = int(input("[] Masukkan pilihan penghapusan (1-3): "))
            
            if pilih_hapus == 1:
                toko.delete_produk_awal()

            elif pilih_hapus == 2:
                toko.delete_produk_akhir()

            elif pilih_hapus == 3:
                nama_produk = input("\n[] Masukkan nama produk yang ingin dihapus: ")
                toko.delete_produk_tengah(nama_produk)

            elif pilihan == 5:
                print("> Terima kasih telah menggunakan program ini!")
                break

            else:
                print("\n> MASUKAN ANGKA YANG TEPAT (1-5)!\n")

    except (ValueError, KeyboardInterrupt, EOFError):
        print("\n> MASUKAN ANGKA!\n")
        break
