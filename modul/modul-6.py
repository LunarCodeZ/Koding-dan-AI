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
print("- Program 1: FIlter bilangan ganjil genap -")
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
print("\n\n- Program 2: Menampilkan nilai perkalian dari masukan nilai -")
bilangan_perkalian = 10
counter_perkalian = 1

while (counter_perkalian <= 10):
    print(f"{bilangan_perkalian} x {counter_perkalian} = {bilangan_perkalian * counter_perkalian}")
    counter_perkalian+=1



# >> Penyelesaian Program 3 <<
# Menampilkan urutan nilai fibonacci
print("\n\n- Program 3: Menampilkan urutan nilai fibonacci -")
nilai = 10 # --> Untuk mengatur banyak nilai
a = 0
b = 0

for n in range(nilai):
    if (n == 0):
        a = 1
        c = a
    elif (n == 1):
        b = 1
    else:
        a = b
        b = c
        c = a + b
    print(c)



# >> Penyelesaian Program 4 <<
# Perkalian nilai 1 - 100
print("\n\n- Program 4: Perkalian nilai 1 - 100 -")
angka = 0
faktor = 1
hasil_perkalian = []

for perkalian in range(10):
    angka+=1
    faktor = 1
    for x in range(10):
        hasil_perkalian.append(angka * faktor)
        faktor+=1
    
    for hasil in range(len(hasil_perkalian)):
        if (hasil < 9):
            print(f"{hasil_perkalian[hasil]},", end=" ")
        else:
            print(hasil_perkalian[hasil])
    hasil_perkalian = []