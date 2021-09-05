# 1. Kondisi selalu berdasarkan logika Benar atau Salah (True atau False)
# 2. Kondisi menggunakan `==`
angka = 10
if angka == 10:
    print('hello python')

# 3. Kondisi menggunakan `and`
angka2 = 12
if angka == 10 and angka2 == 12:
    print('hello python2')

# 4. Kondisi menggunakan `or`
angka3 = 15
if angka == 10 or angka3 == 13:
    print('hello python3')

# 5. Kondisi menggunakan `is` dan `is not`

# 6. Kondisi menggunakan `in` untuk (string | list)
array = [1, 2, 3, 4, 5, 6]
if 5 in array:
    print("5 ada di array")

if "P" in "Python":
    print("P ada di Python")

# 7. Multi-Kondisi menggunakan if-elif-else
umur = 23
if umur > 20:
    print('umur 21')
else:
    print('bukan umur 21')


umur = 50
if umur > 50:
    print('umur > 50')
    if umur == 60:
        print('anda lebih dari 60')
elif umur < 50:
    print('umur < 50')
else:
    print('umur 50')
