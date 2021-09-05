# 1. Fungsi sederhana
def hello():
    print('hello')


hello()

# 2. Fungsi dengan parameter


def hello_nama(nama):
    print('hello{nama}')


hello_nama('python')

# 3. Fungsi dengan return value


def hello_nama2(nama):
    return 'hello{nama}'


hello_nama2('Python 3')
print('nama')
# 4. Task: Buatlah sebuah fungsi untuk menghitung umur dengan parameter tahun lahir


def umur(tahun_lahir):
    return 2021 - tahun_lahir


umur_sekarang = umur(1981)
print(umur_sekarang)
