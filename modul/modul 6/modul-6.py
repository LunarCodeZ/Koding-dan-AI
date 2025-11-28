# =============================
# MODUL 6 - PENGULANGAN
# =============================





# === Latihan ===
print("=== Latihan ===\n")
'''
Buatlah program:
(1) Filter bilangan genap dan ganjil lalu menghitung
    banyak bilangan ganjil dan genap tersebut
(2) Menampilkan nilai perkalian dari masukan nilai
(3) Menampilkan urutan nilai dari fibonacci
(4) Perkalian nilai 1-100
'''



# >> Penyelesaian Program 1 <<
# Filter bilangan genap dan ganjil
# lalu menghitung banyak bilangan ganjil dan genap
print("Program 1: FIlter bilangan ganjil genap")
daftar_bilangan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ganjil = 0
genap = 0

print(f"Daftar Bilangan: {daftar_bilangan}")
for bilangan in daftar_bilangan:
    if (bilangan == daftar_bilangan[-1]):
        print(f"Jumlah bilangan ganjil: {ganjil}")
        print(f"Jumlah bilangan genap: {genap}")
    else:
        if (bilangan % 2 == 0):
            genap+=1
        else:
            ganjil+=1



# >> Penyelesaian Program 2 <<
# Menampilkan nilai perkalian dari masukan nilai
print("\n\n\nProgram 2: Menampilkan nilai perkalian dari masukan nilai")
bilangan_perkalian = 10
counter_perkalian = 1

while (counter_perkalian <= 10):
    print(f"{bilangan_perkalian} x {counter_perkalian} = {bilangan_perkalian * counter_perkalian}")
    counter_perkalian+=1



# >> Penyelesaian Program 3 <<
# Menampilkan urutan nilai fibonacci
print("\n\n\nProgram 3: Menampilkan urutan nilai fibonacci")
# 1, 1, 2, 3, 5, 8, 13, 21, 35
nilai = 1
nilai_pertama = 1
nilai_terakhir = 0
batas_fibonacci = 10
counter_fibonacci = 1

for n in range(10):
    if (n < 2):
        nilai = 1
        print(nilai)
    else:
        nilai_terakhir = nilai
        print(nilai + nilai_terakhir)
        nilai+=1



# >> Penyelesaian Program 4 <<
# Perkalian nilai 1 - 100
print("\n\n\nProgram 4: Perkalian nilai 1 - 100")
angka = 0
faktor = 1
hasil_perkalian = []

for perkalian in range(10):
    angka+=1
    faktor = 1
    for x in range(10):
        hasil_perkalian.append(angka * faktor)
        faktor+=1
    
    print(hasil_perkalian)
    hasil_perkalian = []