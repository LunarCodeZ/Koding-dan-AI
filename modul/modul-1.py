# =============================
# MODUL 1 - MENJALANKAN PYTHON
# =============================

# === Penjelasan Print ===
print("=== Penjelasan Print() ===")

"""
print() ialah syntax atau perintah pada bahasa pemrograman Python yang dapat digunakan
untuk menampilkan teks atau nilai pada suatu variabel.
"""


print("print() menggunakan petik ganda:")
print("Halo dunia\n")

print("print() menggunakan petik tunggal:")
print('Halo dunia\n')


# Menggunakan print untuk menampilkan nilai variabel
nama = "Agus"
umur = 12

print("Menampilkan nilai dari variabel nama:")
print("Nama:",nama,"\n")
print("Menampilkan nilai dari variabel umur:")
print("Umur:",umur,"tahun")



# === Penjelasan Komentar ===

"""
Komentar dapat digunakan untuk menonaktifkan baris kode dan umumnya
juga dapat digunakan untuk menjelaskan suatu kode. Ada 3 cara untuk
menggunakan komentar, yaitu:
(1) Menggunakan simbol pagar (#)
(2) Menggunakan simbol petik ganda (""" """)
(3) Menggunakan simbol petik tunggal (''' ''')
"""

# Ini adalah contoh penggunaan komentar menggunakan simbol pagar,
# komentar ini akan menonaktifkan satu baris kode saja.
# print("Apakah aku ditampilkan ?")

"""
Ini adalah contoh penggunaan komentar menggunakan simbol petik ganda,
komentar ini akan menonaktifkan seluruh baris kode yang berada diantara
tiga pasang petik ganda.

print('Apa aku ditampilkan ?')
"""

'''
Ini adalah contoh penggunaan komentar menggunakan simbol petik tunggal,
komentar ini akan menonaktifkan seluruh baris kode yang berada diantara
tiga pasang petik tunggal.

print('Aku tidak ditampilkan lagi')
'''





# === Latihan ===
print("\n\n\n\n\n=== Latihan ===\n")
'''
(1) Buatlah program yang menampilkan informasi atau biodata anda dengan format
    seperti pada berikut ini:
-------------------------------------------------
Praktikum algoritma dan pemrograman 1
Nama :
NIM : 09081001009
Angkatan : 2008
Jurusan : Sistem Komputer
Fakultas Ilmu Komputer
Universitas Sriwijaya
-------------------------------------------------
lalu berikan juga komentar di setiap baris pada skrip


(2) Menjalankan dan menjelaskan skrip serta outputnya, lalu
    perbaiki jika terdapat error:
-------------------------------------------------
print("Ini Budi") #mencetak penjelasan Budi
print('Budi bersekolah di SDN 1 MariJoa) #sekolah Budi
prnt("Cita - cita ingin menjadi seorang Pilot") #cita-cita budi
-------------------------------------------------
'''


# >> Pengerjaan Latihan 1 <<

print("(1) Informasi biodata:")
print("Praktikum algoritma dan pemrograman 1")
print("Nama: Erik Yanuar Putra") # --> Menampilkan nama
print("Umur: 16 Tahun") # --> Menampilkan umur
print("Kelas: 10") # --> Menampilkan kelas
print("Nis: 11524") # --> Menampilkan nis
print("Jurusan: Rekayasa Perangkat Lunak") # --> Menampilkan jurusan
print("Nama Sekolah: SMKN 2 Buduran") # --> Menampilkan nama sekolah


# >> Pengerjaan Latihan 2 <<
print("\n(2) Memperbaiki dan menampilkan kode:")

# Kode sebelum diperbaiki:
"""
print("Ini Budi") #mencetak penjelasan Budi --> Sudah benar
print('Budi bersekolah di SDN 1 MariJoa) #sekolah Budi --> tidak ada petik penutup sebelum tutup kurung
prnt("Cita - cita ingin menjadi seorang Pilot") #cita-cita budi --> seharusnya print, bukan prnt
"""

# Kode sesudah diperbaiki:
print("Ini Budi") #mencetak penjelasan Budi
print('Budi bersekolah di SDN 1 MariJoa') #sekolah Budi
print("Cita - cita ingin menjadi seorang Pilot") #cita-cita budi
