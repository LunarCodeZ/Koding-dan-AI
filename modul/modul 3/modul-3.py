# =============================
# MODUL 3 - VARIABEL
# =============================





# === Latihan ===
print("=== Latihan ===\n")
'''
(1) Membuat program dengan variabel yang mendeskripsikan biodata, misalnya:
----------------------------------------------------------------------
# biodata
deskripsi ="ini program python"
nama = "Budi Bae"
alamat = "Palembang"
umur = 20
hobi = "makan"
dengan output sebagai berikut:
Nama saya Budi Bae yang beralamat di Palembang, umur sekarang 20 tahun
dan memiliki hobi makan
----------------------------------------------------------------------

(2) Memuat program yang dapat menghitung luas dan keliling persegi panjang
----------------------------------------------------------------------
# menghitung luas & keliling persegi panjang
panjang = 15
lebar = 5.7
keliling_persegi_panjang = panjang*lebar
lebar_persegi_panjang = 2*(panjang+lebar)
dengan output sebagai berikut:
Sebuah persegi panjang memiliki panjang 15 cm,
lebar 5.7 cm dan memiliki luas sebesar 85.5 cm dan keliling 41.4 cm
----------------------------------------------------------------------
'''


# >> Pengerjaan Latihan 1 <<
# Biodata
deskripsi = "Ini adalah program Python"
nama = "Erik Yanuar Putra"
alamat = "Sidoarjo"
umur = 16
hobi = "Coding dan bermain game"

# Output:
print(f"Nama saya ialah {nama} yang beralamat di {alamat}. Umur saya sekarang ialah {umur} tahun, serta memiliki hobi yaitu {hobi}")



# >> Pengerjaan Latihan 2 <<
# Menghitung Luas & Keliling Persegi Panjang
panjang = 20
lebar = 5.7
keliling_persegi_panjang = 2 * (panjang + lebar)
luas_persegi_panjang = panjang * lebar

# Output:
print("Sebuah persegi panjang memiliki:")
print(f"Panjang: {panjang} cm,")
print(f"Lebar: {lebar} cm")
print(f"Sehingga kelilingnya ialah: {keliling_persegi_panjang} cm dan luasnya ialah: {luas_persegi_panjang} cm")