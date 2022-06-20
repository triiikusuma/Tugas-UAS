from prettytable import PrettyTable
import mysql.connector

koneksi = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="programming"
)

active = True

while active:
    programming = koneksi.cursor()

    programming.execute('select*from mahasiswa')

    data = programming.fetchall()
    t = PrettyTable(['id', 'nama', 'nim'])

    for row in data:
        t.add_row(row)
    print(t)

    print("menu pilihan : ")
    print("1. Insert data")
    print("2. Update Data")
    print("3. Delete Data")
    print("4. Exit")
    inputuser = input("\nMasukkan data yang Diberikan : ")

    if inputuser == '1':
        nama = input("Masukkan Nama : ")
        nim = input("Masukkan NIM  : ")

        if len(nama) == 0 and len(nim) == 0:
            print("Data Kosong")
        else:
            koneksiTest = koneksi.cursor()

            koneksiTest.execute(
                "insert into mahasiswa (nama, nim) VALUES (%s, %s)", (nama, nim))

            koneksi.commit()

            print("Data Berhasil Ditambahkan")
        cek = input("Apa Anda Ingin Melanjutkan data Kembali? (Ya/Tidak) :")
        if cek == 'Tidak':
            active = False
    if inputuser == '2':
        idupdate = input("Masukkan Id yang ingin diupdate : ")
        print("Pilih tabel yang ingin diupdate : ")
        print("1. Nama")
        print("2. NIM")
        print("3. Ubah Semuanya")
        aksiupdate = input("Pilih 1-3 : ")
        if aksiupdate == '1':
            namaupdate = input("Masukkan Nama Baru : ")
            koneksiTest = koneksi.cursor()
            koneksiTest.execute(
                f"update mahasiswa set nama = '{namaupdate}' where id = '{idupdate}'")
            koneksi.commit()
            print("Data Nama Berhasil Diupdate")
        elif aksiupdate == '2':
            nimupdate = input("Masukkan NIM Baru : ")
            koneksiTest = koneksi.cursor()
            koneksiTest.execute(
                f"update mahasiswa set nim = '{nimupdate}' where id = '{idupdate}'")
            koneksi.commit()
            print("Data NIM Berhasil Diupdate")
        elif aksiupdate == '3':
            namaupdate = input("Masukkan Nama Baru : ")
            nimupdate = input("Masukkan NIM Baru : ")
            koneksiTest = koneksi.cursor()
            koneksiTest.execute(
                f"update mahasiswa set nama = '{namaupdate}', nim = '{nimupdate}' where id = '{idupdate}'")
            koneksi.commit()
            print("Data Berhasil Diupdate")
        else:
            print("Masukkan 1-3")

        cek = input("Apa Anda Ingin Melanjutkan data Kembali? (Ya/Tidak) : ")
        if cek == 'Tidak':
            active = False
    if inputuser == '3':
        iddelete = input("Masukkan ID yang ingin dihilangkan : ")
        koneksiTest = koneksi.cursor()
        koneksiTest.execute(
            f"delete from mahasiswa where id='{iddelete}'")
        koneksi.commit()
        print("Data Berhasil Dihilangkan")
        cek = input("Apa Anda Ingin Melanjutkan data Kembali? (Ya/Tidak) : ")
        if cek == 'Tidak':
            active = False
    if inputuser == '4':
        active = False