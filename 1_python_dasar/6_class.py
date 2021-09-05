
# Semua tipe di Python adalah Object
# Class atau Kelas digunakan untuk membungkus logika / bussiness-logic yang mempunyai fungsi khusus tertentu, atau mempresentasikan sebuah object.
# Apakah harus memakai class?
# Kapan harus membuat class?

# 1. Class dan Object
# 2. Class dengan properti (variable)
# 3. Class dengan method (fungsi)
# 3. Class anakan (sub-class)

class User:
    nama_depan = "Rifky"
    nama_belakang = "Alamsyah"
    umur = 21

    def nama_lengkap(self):
        return self.nama_depan + self.nama_belakang


user = User()

print(user.nama_lengkap())
print(user.umur)
