import os
import math
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
        self.sort_by = None
        self.tail = None
        self.length = 0  # Inisialisasi panjang linked list

    def jump_search_by_nama(self, nama_produk):
        length = self.get_length()
        if length == 0:
            return None

        block_size = int(length ** 0.5)
        current_node = self.head
        prev_node = None

        while current_node and current_node.data["nama_produk"] < nama_produk:
            prev_node = current_node
            for _ in range(min(block_size, length)):
                if current_node.next:
                    current_node = current_node.next
            length -= block_size  # Perbarui nilai length setiap iterasi

        while prev_node and prev_node.data["nama_produk"] < nama_produk:
            prev_node = prev_node.next

        if prev_node and prev_node.data["nama_produk"] == nama_produk:
            return prev_node
        else:
            return None


    def search_by_nama(self, nama_produk):
        result = self.jump_search_by_nama(nama_produk)
        if result:
            print("Produk ditemukan:")
            table = PrettyTable(["Nama Produk", "Deskripsi", "Harga", "Stok", "Jenis Bahan"])
            produk = result.data
            table.add_row([produk["nama_produk"], produk["deskripsi"], f"Rp{produk['harga']}", produk["stok"], produk["jenis_bahan"]])
            print(table)
        else:
            print("Produk tidak ditemukan.")

    def jump_search_by_material(self, jenis_bahan):
        length = self.get_length()
        if length == 0:
            return None

        block_size = int(length ** 0.5)
        current_node = self.head
        prev_node = None

        while current_node and current_node.data["jenis_bahan"] < jenis_bahan:
            prev_node = current_node
            for _ in range(min(block_size, length)):
                if current_node.next:
                    current_node = current_node.next
            length -= block_size  # Perbarui nilai length setiap iterasi

        while prev_node and prev_node.data["jenis_bahan"] < jenis_bahan:
            prev_node = prev_node.next

        if prev_node and prev_node.data["jenis_bahan"] == jenis_bahan:
            return prev_node
        else:
            return None

    def search_by_material(self, jenis_bahan):
        result = self.jump_search_by_material(jenis_bahan)
        if result:
            print("Produk ditemukan:")
            table = PrettyTable(["Nama Produk", "Deskripsi", "Harga", "Stok", "Jenis Bahan"])
            produk = result.data
            table.add_row([produk["nama_produk"], produk["deskripsi"], f"Rp{produk['harga']}", produk["stok"], produk["jenis_bahan"]])
            print(table)
        else:
            print(f"Tidak ditemukan produk dengan jenis bahan '{jenis_bahan}'.")
            
    # def sort_produk(self):
    #     if not self.head:
    #         os.system("cls")
    #         print("Tidak ada produk untuk diurutkan.")
    #         a = input("Tekan Enter untuk kembali ke menu sebelumnya")
    #         if a == "":
    #             os.system('cls')
    #         return
    #     print(" Menu Sorting Produk:")
    #     print("1. Sorting berdasarkan Nama Produk (Ascending)")
    #     print("2. Sorting berdasarkan Nama Produk (Descending)")
    #     print("3. Sorting berdasarkan Jenis Bahan (Ascending)")
    #     print("4. Sorting berdasarkan Jenis Bahan (Descending)")
    #     print("5. Kembali ke Menu Utama")
        
    #     choice = input("Pilih opsi: ")
    #     if choice == "1":
    #         self.sortAscendingJudul()
    #         self.show_produk()
    #         a = input("Tekan Enter untuk kembali ke menu sebelumnya")
    #         if a == "":
    #             os.system('cls')
    #     elif choice == "2":
    #         self.sortDescendingJudul()
    #         self.show_produk()
    #         a = input("Tekan Enter untuk kembali ke menu sebelumnya")
    #         if a == "":
    #             os.system('cls')
    #     elif choice == "3":
    #         self.sortAscendingBahan()
    #         self.show_produk()
    #         a = input("Tekan Enter untuk kembali ke menu sebelumnya")
    #         if a == "":
    #             os.system('cls')
    #     elif choice == "4":
    #         self.sortDescendingBahan()
    #         self.show_produk()
    #         a = input("Tekan Enter untuk kembali ke menu sebelumnya")
    #         if a == "":
    #             os.system('cls')
    #     elif choice == "5":
    #         print("Kembali ke Menu Utama.")
    #     else:
    #         print("Opsi tidak valid.")
    #         a = input("Tekan Enter untuk kembali ke menu sebelumnya")
    #         if a == "":
    #             os.system('cls')

    def quickSortJudul(self, head):
        if head is None or head.next is None:
            return head
        pivot = head
        smallerHead = None
        equalHead = pivot
        largerHead = None
        current = head.next
        while current is not None:
            nextNode = current.next
            if current.data["nama_produk"] < pivot.data["nama_produk"]:
                current.next = smallerHead
                smallerHead = current
            elif current.data["nama_produk"] == pivot.data["nama_produk"]:
                current.next = equalHead
                equalHead = current
            else:
                current.next = largerHead
                largerHead = current
            current = nextNode
        smallerHead = self.quickSortJudul(smallerHead)
        largerHead = self.quickSortJudul(largerHead)
        if smallerHead is not None:
            temp = smallerHead
            while temp.next is not None:
                temp = temp.next
            temp.next = equalHead
        else:
            smallerHead = equalHead
        pivot.next = largerHead if largerHead is not None else None
        return smallerHead

    def sortAscendingJudul(self):
        self.head = self.quickSortJudul(self.head)

    def sortDescendingJudul(self):
        self.sortAscendingJudul()
        prev = None
        current = self.head
        while current is not None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        self.head = prev

    def quickSortBahan(self, head):
        if head is None or head.next is None:
            return head
        pivot = head
        smallerHead = None
        equalHead = pivot
        largerHead = None
        current = head.next
        while current is not None:
            nextNode = current.next
            if current.data["jenis_bahan"] < pivot.data["jenis_bahan"]:
                current.next = smallerHead
                smallerHead = current
            elif current.data["jenis_bahan"] == pivot.data["jenis_bahan"]:
                current.next = equalHead
                equalHead = current
            else:
                current.next = largerHead
                largerHead = current
            current = nextNode
        smallerHead = self.quickSortBahan(smallerHead)
        largerHead = self.quickSortBahan(largerHead)
        if smallerHead is not None:
            temp = smallerHead
            while temp.next is not None:
                temp = temp.next
            temp.next = equalHead
        else:
            smallerHead = equalHead
        pivot.next = largerHead if largerHead is not None else None
        return smallerHead

    def sortAscendingBahan(self):
        self.head = self.quickSortBahan(self.head)

    def sortDescendingBahan(self):
        self.sortAscendingBahan()
        prev = None
        current = self.head
        while current is not None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        self.head = prev
        
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

    def get_length(self):
        return self.length

    def data_record(self, nama_produk, deskripsi, harga, stok, jenis_bahan):
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
        self.length += 1  # Menambah panjang linked list saat menambahkan node baru

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

toko.data_record(
    "",
    "Data dummy, agar dapat menjalankan searchin",
    0,
    0,
    ""
)
toko.data_record(
    "Kursi Sofa",
    "Kursi sofa minimalis dengan bahan kain katun yang nyaman, cocok untuk ruang tamu.",
    1500000,
    10,
    "Kain Katun"
)
toko.data_record(
    "Meja Makan",
    "Meja makan terbuat dari kayu jati solid dengan desain modern, cocok untuk 4-6 orang.",
    3000000,
    5,
    "Kayu Jati"
)
toko.data_record(
    "Lemari Pakaian",
    "Lemari pakaian dengan 3 pintu dan 2 laci, terbuat dari kayu MDF dengan finishing cat putih.",
    2000000,
    8,
    "Kayu MDF"
)
toko.data_record(
    "Kursi Sofa Panjang",
    "Kursi sofa dengan bantalan empuk, dicat dengan warna kayu.",
    1700000,
    4,
    "Ulin"
)
toko.data_record(
    "Ayunan",
    "Ayunan dengan kursi berhadapan, dicat dengan warna alami.",
    11000000,
    7,
    "Mahoni"
)
toko.data_record(
    "",
    "Data dummy, agar dapat menjalankan searching",
    0,
    0,
    ""
)

while True:
    print("" )
    print("=" * 35)
    print("           Halo admin        ")
    print(f"Selamat datang di {toko.nama_toko}")
    print("=" * 35)
    print("Menu:")
    print("1. Tambah Produk")
    print("2. Tampilkan Produk")
    print("3. Perbarui Produk")
    print("4. Hapus Produk")
    print("5. Mengurutkan")
    print("6. Cari Produk")
    print("7. Keluar")

    try:
        pilihan = int(input("[] Masukkan pilihan Anda (1-7): "))

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
            print(" \nMenu Sorting Produk:")
            print("1. Sorting berdasarkan Nama Produk (Ascending)")
            print("2. Sorting berdasarkan Nama Produk (Descending)")
            print("3. Sorting berdasarkan Jenis Bahan (Ascending)")
            print("4. Sorting berdasarkan Jenis Bahan (Descending)")
            print("0. Kembali ke Menu Utama")
            
            choice = input("Pilih opsi: ")
            if choice == "1":
                toko.sortAscendingJudul()
                toko.show_produk()
                a = input("Tekan Enter untuk kembali ke menu sebelumnya")
                if a == "":
                    os.system('cls')
            elif choice == "2":
                toko.sortDescendingJudul()
                toko.show_produk()
                a = input("Tekan Enter untuk kembali ke menu sebelumnya")
                if a == "":
                    os.system('cls')
            elif choice == "3":
                toko.sortAscendingBahan()
                toko.show_produk()
                a = input("Tekan Enter untuk kembali ke menu sebelumnya")
                if a == "":
                    os.system('cls')
            elif choice == "4":
                toko.sortDescendingBahan()
                toko.show_produk()
                a = input("Tekan Enter untuk kembali ke menu sebelumnya")
                if a == "":
                    os.system('cls')
            elif choice == "0":
                print("Kembali ke Menu Utama.")
            else:
                print("Opsi tidak valid.")
                a = input("Tekan Enter untuk kembali ke menu sebelumnya")
                if a == "":
                    os.system('cls')

        elif pilihan == 6:
            print("\n1. Cari Produk berdasarkan Nama")
            print("2. Cari Produk berdasarkan Jenis Bahan")
            pilih_cari = int(input("[] Masukkan pilihan pencarian (1-2): "))
            
            if pilih_cari == 1:
                nama_produk = input("\n[] Masukkan nama produk yang ingin dicari: ")
                toko.sortAscendingJudul()
                toko.search_by_nama(nama_produk)
            elif pilih_cari == 2:
                jenis_bahan = input("\n[] Masukkan jenis bahan produk yang ingin dicari: ")
                toko.sortAscendingBahan()
                toko.search_by_material(jenis_bahan)
        
        elif pilihan == 7:
            os.system('cls')
            print("\n> Terima kasih telah menggunakan program ini!\n")
            break

    except (ValueError, KeyboardInterrupt, EOFError):
        print("\n> MASUKAN ANGKA!\n")
        break
