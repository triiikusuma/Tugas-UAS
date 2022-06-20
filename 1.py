mahasiswa = [
    {
        "nama": "Tri Kusuma",
        "nimMahasiswa": "421313252",
        "Jurusan": "Teknologi Informasi"
    },
    {
        "nama": "Pande Priatama",
        "nimMahasiswa": "421313253",
        "Jurusan": "Teknologi Informasi"
    },
    {
        "nama": "Adi Saputra",
        "nimMahasiswa": "421313254",
        "Jurusan": "Teknologi Informasi"
    }

]

print("Silahkan Pilih nama Mahasiswa Berikut : ")
print("1. Tri Kusuma")
print("2. Pande Priatama")
print("3. Adi Saputra")

input = input("\nMasukkan Angka 1-3 :")


if input == '1':
    print("nama = ", mahasiswa[0]['nama'])
    print("nimMahasiswa = ", mahasiswa[0]['nimMahasiswa'])
    print("Jurusan = ", mahasiswa[0]['Jurusan'])

elif input == '2':
    print("nama = ", mahasiswa[1]['nama'])
    print("nimMahasiswa = ", mahasiswa[1]['nimMahasiswa'])
    print("Jurusan = ", mahasiswa[1]['Jurusan'])
else:
    print("nama = ", mahasiswa[2]['nama'])
    print("nimMahasiswa = ", mahasiswa[2]['nimMahasiswa'])
    print("Jurusan = ", mahasiswa[2]['Jurusan'])
