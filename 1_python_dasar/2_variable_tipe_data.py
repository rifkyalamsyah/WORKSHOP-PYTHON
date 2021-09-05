# 1. Variable - menampung data

# 2. Python = dynamically typed language, buat variable saat diperlukan
nama = "Rifky"
umur = 21

# 3. tipe = Boolean (benar / salah)
Benar = True
Salah = False
benar2 = not False

print(Benar)
print(Salah)
print(benar2)

# 5. tipe - Number/Angka (bilangan bulat | pecahan | negatif)
bil_bulat = 10
bil_pecahan = 0.95
bil_negatif = -10

print(bil_bulat)
print(bil_pecahan)
print(bil_negatif)

# 6. tipe - Number/Angka (operasi matematika | tambah | kurang | kali | bagi | pangkat)
a = 10
b = 15

tambah = a + b
print(tambah)

kurang = a - b
print(kurang)

kali = a * b
print(kali)

bagi = a / b
print(bagi)

pangkat = 2 ** 3
print(pangkat)

# 7. tipe - String ('...' atau "...")
nama_depan = "Rifky "

# 8. tipe - String (menggabungkan string)
nama_belakang = "Alamsyah"

nama_lengkap = nama_depan + nama_belakang
print(nama_lengkap)

# 9. tipe - String (memformat string, upper case, lowercase)
print("Python".upper())
print("Python".lower())

nama = "Python"
halo = "hallo nama saya adalah {nama}"
print(halo)

# 10. tipe - List (seperti array, menampung apa saja)
daftar_angka = [1, 2, 3, 4, 5, 6, 7]
daftar_angka_str = ["satu", "dua", "tiga"]
daftar_angka_campuran = [1, "dua", 3]

# 11. tipe - List (mengakses, menambah, menghapus isi list)
print(daftar_angka[0])
print(daftar_angka[6])
print(daftar_angka[0:3])  # slicing / menampilkan beberapa bagian

# menambah data ke list
daftar_angka_baru = daftar_angka.append(10)
print(daftar_angka)

# menghapus data ke list
daftar_angka.pop(0)
print(daftar_angka)

# 12. tipe - List (menggabungkan isi list)
list1 = [1, 2, 3, 4]
list2 = [4, 5, 6]
print(list1 + list2)

# 13. tipe - Dictionary (map, key-value)
buah = {
    'nama': 'durian',
    'tinggi': 10
}

# 14. tipe - Dictionary (membuat, mengisi, mengakses, menghapus isi dict)
buah2 = {}
buah2['nama'] = 'apple'
buah2['tinggi'] = 5

print(buah2['nama'])
print(buah2['tinggi'])
