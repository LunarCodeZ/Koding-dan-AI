# =============================
# MODUL 2 - TIPE DATA
# =============================

# === Penjelasan Tipe Data ===

"""
Tipe data ialah jenis data yang terdapat pada suatu variabel.
Pada bahasa pemrograman Python, ada 10, antara lain yaitu:
- Boolean
- String
- Integer
- Float
- Binary
- Octal
- Hexadecimal
- List
- Tuple
- Dictionary
"""

# Contoh penggunaan tipe data
"""
nama = "Budi" # --> String
umur = 20  # --> Integer
laki_laki = True  # --> Boolean
nilai = 85.8  # --> Float
keranjang = ["Apel", "Jeruk", "Nanas"]  # --> List
hewan_peliharaan = {  # --> Dictionary
    'nama': "Aron",
    'hewan': "Kucing",
    'umur': 6
}

biner = 0b10  # --> Binary
oktal = 0o10  # --> Octal
heksadesimal = 0x10  # --> Hexadecimal
compleks = 1 + 5j  # --> Complex
"""





# === Latihan ===
print("=== Latihan ===\n")
'''
(1) Membuat program yang menggunakan variabel dan tipe data
    serta menampilkan output seperti berikut:
---------------------------------------------------------------
Praktikum Algoritma dan Pemrograman 1 - Variable dan Tipe Data
False
<class 'bool'>
Ini adalah tulisan berupa String
100
0.001
bilangan desimal dari 0x01 adalah 1
10
<class 'complex'>
(2+6j)
<class 'complex'>
[96, 97, 98, 99, 100]
['seratus', 'dua ratus', 'tiga ratus']
{'nama': 'Ani', 'umur': 19}
This string contains a single quote (') character.
---------------------------------------------------------------

(2) Menjelaskan output dari file boolean.py dan string_format.py
'''


# >> Pengerjaan Latihan 1 <<

boolean = False
tulisan = "Ini adalah tulisan berupa String"
nilai = 100
desimal = 0.001
heksadesimal = 0x01
angka = 10
kompleks = 2 + 6j
daftar = [96, 97, 98, 99, 100]
daftar_kata = ['seratus', 'dua ratus', 'tiga ratus']
dictionary = {
    'nama': 'Ani',
    'umur': 19
}

print("(1) Program menggunakan variabel dan tipe data:")
print("Praktikum Algoritma dan Pemrograman 1 - Variabel dan Tipe Data")
print(boolean)
print(tulisan)
print(f"Bilangan desimal dari 0x01 adalah {heksadesimal}")
print(angka)
print(type(kompleks))
print(kompleks)
print(type(kompleks))
print(daftar)
print(daftar_kata)
print(dictionary)
print('Kalimat ini mengandung simbol petik tunggal (\')')