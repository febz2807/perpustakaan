# =====================================================
# PROGRAM PBL: SISTEM PERPUSTAKAAN SEDERHANA
# Nama  : Febryanto Nugroho
# NPM   : 202243500473
# Kelas : S6D - Teknik Informatika (Unindra)
# =====================================================

anggota = []
buku = []
peminjaman = []

def tambah_anggota():
    print("\n=== Tambah Anggota ===")
    id_anggota = input("ID Anggota: ")
    nama = input("Nama Anggota: ")
    alamat = input("Alamat: ")
    anggota.append({"id": id_anggota, "nama": nama, "alamat": alamat})
    print("Anggota berhasil ditambahkan!\n")

def tambah_buku():
    print("\n=== Tambah Buku ===")
    id_buku = input("ID Buku: ")
    judul = input("Judul Buku: ")
    penulis = input("Penulis: ")
    buku.append({"id": id_buku, "judul": judul, "penulis": penulis})
    print("Buku berhasil ditambahkan!\n")

def tampil_anggota():
    print("\n=== Data Anggota ===")
    if not anggota:
        print("Belum ada data anggota.\n")
        return
    for a in anggota:
        print(f"ID: {a['id']} | Nama: {a['nama']} | Alamat: {a['alamat']}")
    print()

def tampil_buku():
    print("\n=== Data Buku ===")
    if not buku:
        print("Belum ada data buku.\n")
        return
    for b in buku:
        print(f"ID: {b['id']} | Judul: {b['judul']} | Penulis: {b['penulis']}")
    print()

def peminjaman_buku():
    print("\n=== Peminjaman Buku ===")
    id_anggota = input("Masukkan ID Anggota: ")
    id_buku = input("Masukkan ID Buku: ")
    tanggal_pinjam = input("Tanggal Pinjam (dd/mm/yyyy): ")

    # Validasi data
    cari_anggota = next((a for a in anggota if a['id'] == id_anggota), None)
    cari_buku = next((b for b in buku if b['id'] == id_buku), None)

    if not cari_anggota:
        print("Anggota tidak ditemukan!")
        return
    if not cari_buku:
        print("Buku tidak ditemukan!")
        return

    peminjaman.append({
        "id_anggota": id_anggota,
        "id_buku": id_buku,
        "tanggal_pinjam": tanggal_pinjam
    })
    print("Peminjaman berhasil dicatat!\n")

def tampil_peminjaman():
    print("\n=== Data Peminjaman ===")
    if not peminjaman:
        print("Belum ada data peminjaman.\n")
        return
    for p in peminjaman:
        print(f"Anggota: {p['id_anggota']} | Buku: {p['id_buku']} | Tanggal: {p['tanggal_pinjam']}")
    print()

def hapus_data():
    print("\n=== Hapus Data ===")
    print("1. Hapus Anggota")
    print("2. Hapus Buku")
    pilihan = input("Pilih data yang ingin dihapus: ")

    if pilihan == "1":
        id_anggota = input("Masukkan ID Anggota: ")
        for a in anggota:
            if a["id"] == id_anggota:
                anggota.remove(a)
                print("Data anggota berhasil dihapus!\n")
                return
        print("Data anggota tidak ditemukan.\n")

    elif pilihan == "2":
        id_buku = input("Masukkan ID Buku: ")
        for b in buku:
            if b["id"] == id_buku:
                buku.remove(b)
                print("Data buku berhasil dihapus!\n")
                return
        print("Data buku tidak ditemukan.\n")
    else:
        print("Pilihan tidak valid.\n")

def main():
    while True:
        print("===== SISTEM PERPUSTAKAAN =====")
        print("1. Tambah Anggota")
        print("2. Tambah Buku")
        print("3. Tampilkan Anggota")
        print("4. Tampilkan Buku")
        print("5. Peminjaman Buku")
        print("6. Tampilkan Data Peminjaman")
        print("7. Hapus Data")
        print("8. Keluar")

        pilih = input("Pilih menu (1-8): ")

        if pilih == "1":
            tambah_anggota()
        elif pilih == "2":
            tambah_buku()
        elif pilih == "3":
            tampil_anggota()
        elif pilih == "4":
            tampil_buku()
        elif pilih == "5":
            peminjaman_buku()
        elif pilih == "6":
            tampil_peminjaman()
        elif pilih == "7":
            hapus_data()
        elif pilih == "8":
            print("Terima kasih telah menggunakan sistem ini!")
            break
        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    main()
