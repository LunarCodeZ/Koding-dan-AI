# =============================
# MODUL 4 - OPERATOR
# =============================





# === Latihan ===
print("=== Latihan ===\n")
'''
Membuat program menggunakan operator dan tipe data
dengan skenario sebagai berikut:
----------------------------------------------------------------------
# program 1: perhitungan sederhana
BilanganPertama = 15
BilanganKedua = 8
BilanganKetiga = 100
RumusPengjumlahan = BilanganPertama + BilanganKedua + BilanganKetiga
RumusPengurangan ?
RumusPerkalian ?

dengan output sebagai berikut:

Penjumlahan = 15 + 8 + 100 = ?
Pengurangan = 15 - 8 - 100 = ?
Perkalian = 15 x 8 x 100 = ?
----------------------------------------------------------------------

----------------------------------------------------------------------
# program 2: menghitung luas bangun datar
# 1. Luas Persegi
panjang_sisi = 20
luas_persegi = panjang_sisi * panjang_sisi
# 2. Luas Persegi Panjang
panjang_pp = 50
lebar_pp = 25.5
luas_pp = panjang_pp * lebar_pp
# 3. Luas Segitiga
alas_segitiga = 40
tinggi_segitiga = 60
luas_segitiga = 0.5*alas_segitiga*tinggi_segitiga
# Lanjutkan untuk luas lingkaran, luas jajaran genjang dan trapesium

tampilkan output, berupa nilai variabel nya masing - masing
----------------------------------------------------------------------

----------------------------------------------------------------------
# program 3, buatlah program nya dengan output seperti pada gambar
# di bawah, gunakan operator bitwise, dengan menentukan berapakah nilai
# variabel a, b dengan nilai output seperti pada gambar
----------------------------------------------------------------------
'''


# >> Penyelesaian Program 1 <<
# Perhitungan Sederhana
print("Program 1: Perhitungan Sederhana")
bilangan_pertama = 15
bilangan_kedua = 8
bilangan_ketiga = 100
penjumlahan = bilangan_pertama + bilangan_kedua + bilangan_ketiga
pengurangan = bilangan_pertama - bilangan_kedua - bilangan_ketiga
perkalian = bilangan_pertama * bilangan_kedua * bilangan_ketiga

# Output:
print(f"Penjumlahan: {bilangan_pertama} + {bilangan_kedua} + {bilangan_ketiga} = {penjumlahan}")
print(f"Pengurangan: {bilangan_pertama} - {bilangan_kedua} - {bilangan_ketiga} = {pengurangan}")
print(f"Perkalian: {bilangan_pertama} * {bilangan_kedua} * {bilangan_ketiga} = {perkalian}")



# >> Penyelesaian Program 2 <<
# Luas Bangun Datar
print("\n\n\nProgram 2: Luas Bangun Datar")
# 1. Luas Bangun Datar Persegi:
panjang_sisi = 20
luas_persegi = panjang_sisi * panjang_sisi

# 2. Luas Bangun Datar Persegi Panjang:
panjang_pp = 50
lebar_pp = 25.5
luas_pp = panjang_pp * lebar_pp

# 3. Luas Bangun Datar Segitiga:
alas_segitiga = 40
tinggi_segitiga = 60
luas_segitiga = 0.5 * alas_segitiga * tinggi_segitiga # --> Ditulis 0.5 karena 1/2 = 0.5

# 4. Luas Bangun Datar Lingkaran:
jari_jari_lingkaran = 30
luas_lingkaran = 3.14 * (jari_jari_lingkaran * jari_jari_lingkaran)

# 5. Luas Bangun Datar Jajar Genjang:
alas_jajar_genjang = 20
tinggi_jajar_genjang = 15
luas_jajar_genjang = alas_jajar_genjang * tinggi_jajar_genjang

# 6. Luas Bangun Datar Trapesium:
sisi_sejajar_1_trapesium = 12
sisi_sejajar_2_trapesium = 20
tinggi_trapesium = 10
luas_trapesium = 0.5 * (sisi_sejajar_1_trapesium + sisi_sejajar_2_trapesium) * tinggi_trapesium



# Output:
print("Luas Bangun Datar Persegi:")
print(f"Sisi Persegi: {panjang_sisi} cm")
print(f"Luas Persegi: Sisi * Sisi")
print(f"Luas Persegi: {panjang_sisi} cm * {panjang_sisi} cm")
print(f"Luas Persegi: {luas_persegi} cm")

print("\nLuas Bangun Datar Persegi Panjang:")
print(f"Panjang Persegi Panjang: {panjang_pp} cm")
print(f"Lebar Persegi Panjang: {lebar_pp} cm")
print(f"Luas Persegi Panjang: Panjang * Lebar")
print(f"Luas Persegi Panjang: {panjang_pp} cm * {lebar_pp} cm")
print(f"Luas Persegi Panjang: {luas_pp} cm")

print("\nLuas Bangun Datar Segitiga:")
print(f"Alas Segitiga: {alas_segitiga} cm")
print(f"Tinggi Segitiga: {tinggi_segitiga} cm")
print(f"Luas Segitiga: 0.5 * Alas * Tinggi")
print(f"Luas Segitiga: 0.5 * {alas_segitiga} cm * {tinggi_segitiga} cm")
print(f"Luas Segitiga: {luas_segitiga} cm")

print("\nLuas Bangun Datar Lingkaran:")
print(f"Jari-jari Lingkaran: {jari_jari_lingkaran} cm")
print(f"Luas Lingkaran: Phi * (Jari-jari * Jari-jari)")
print(f"Luas Lingkaran: 3.14 cm * ({jari_jari_lingkaran} cm * {jari_jari_lingkaran} cm)")
print(f"Luas Lingkaran: {luas_lingkaran} cm")

print("\nLuas Bangun Datar Jajar Genjang:")
print(f"Alas Jajar Genjang: {alas_jajar_genjang} cm")
print(f"Tinggi Jajar Genjang: {tinggi_jajar_genjang} cm")
print(f"Luas Jajar Genjang: Alas * Tinggi")
print(f"Luas Jajar Genjang: {alas_jajar_genjang} cm * {tinggi_jajar_genjang} cm")
print(f"Luas Jajar Genjang: {luas_jajar_genjang} cm")

print("\nLuas Bangun Datar Trapesium:")
print(f"Sisi A Trapesium: {sisi_sejajar_1_trapesium} cm")
print(f"Sisi B Trapesium: {sisi_sejajar_2_trapesium} cm")
print(f"Tinggi Trapesium: {tinggi_trapesium} cm")
print(f"Luas Trapesium: 0.5 * (Sisi A + Sisi B) * Tinggi")
print(f"Luas Trapesium: 0.5 * ({sisi_sejajar_1_trapesium} cm + {sisi_sejajar_2_trapesium} cm) * {tinggi_trapesium} cm")
print(f"Luas Trapesium: {luas_trapesium} cm")



# >> Penyelesaian Program 3 <<
# Program Operator Bitwise
print("\n\n\nProgram 3: Program Operator Bitwise")

# Output: