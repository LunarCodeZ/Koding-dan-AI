# =============================
# MODUL 5 - KONDISI
# =============================





# === Latihan ===
print("=== Latihan ===\n")
'''
(1) Membuat program menggunakan kondisi (if, else, elif)
    dengan skenario:
a. Program 1 - Mengecek apakah segitiga tersebut merupakan:
   > Segitiga sama sisi
   > Segitiga sama kaki
   > Segitiga sembarang
'''



# >> Penyelesaian Program 1 <<
# Cek Segitiga
print("Program 1: Cek Segitiga")
x = 10
y = 10
z = 10

print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")

if (x == y and x == z and y == z):
    print("Hasil: Segitiga sama sisi")
    print(f"Karena x={x}, y={y}, dan z={z} memiliki nilai sisi yang sama")
elif (x != y and y != z and z != x):
    print("Hasil: Segitiga sembarang")
    print(f"Karena x={x}, y={y}, dan z={z} memiliki nilai sisi yang masing-masing berbeda")
else:
    print("Hasil: Segitiga sama kaki")
    print(f"Karena x={x}, y={y}, dan z={z} memiliki salah satu nilai sisi yang berbeda")



# >> Penyelesaian Program 2 <<
# Cek Tahun Kabisat
print("\n\n\nProgram 2: Cek Tahun Kabisat")
tahun = 2002

print(f"Tahun: {tahun}")

if (tahun % 4 == 0):
    print(f"Tahun {tahun}, adalah tahun kabisat !")
else:
    print(f"Tahun {tahun}, bukan tahun kabisat !")



# >> Penyelesaian Program 3 <<
# Zodiak / Astrologi Yunani
print("\n\n\nProgram 3: Zodiak / Astrologi Yunani")
tanggal = 22
bulan = "Juni"
daftar_bulan = [
    "Januari", "Februari", "Maret", "April", "Mei", "Juni",
    "Juli", "Agustus", "September", "Oktober", "November", "Desember"
]

print(f"Tanggal Lahir: {tanggal}")
print(f"Bulan Lahir: {bulan}")

if ((bulan in daftar_bulan)):

    if (bulan == 1 or bulan == daftar_bulan[0]):
        if (tanggal > 0 and tanggal <= 31):
            if (tanggal > 0 and tanggal < 20):
                print("Astrologi anda ialah: Capricorn")
            else:
                print("Astrologi anda ialah: Aquarius")
        else:
            print(f"Bulan Januari tidak memiliki tanggal {tanggal} !")
            print("Bulan ini hanya memiliki tanggal 1 - 31 saja")
    
    elif (bulan == 2 or bulan == daftar_bulan[1]):
        if (tanggal > 0 and tanggal <= 28):
            if (tanggal > 0 and tanggal < 19):
                print("Astrologi anda ialah: Aquarius")
            else:
                print("Astrologi anda ialah: Pisces")
        else:
            print(f"Bulan Februrari tidak memiliki tanggal {tanggal} !")
            print("Bulan ini hanya memiliki tanggal 1 - 28 saja")

    elif (bulan == 3 or bulan == daftar_bulan[2]):
        if (tanggal > 0 and tanggal <= 31):
            if (tanggal > 0 and tanggal < 21):
                print("Astrologi anda ialah: Pisces")
            else:
                print("Astrologi anda ialah: Aries")
        else:
            print(f"Bulan Maret tidak memiliki tanggal {tanggal} !")
            print("Bulan ini hanya memiliki tanggal 1 - 31 saja")

    elif (bulan == 4 or bulan == daftar_bulan[3]):
        if (tanggal > 0 and tanggal <= 30):
            if (tanggal > 0 and tanggal < 20):
                print("Astrologi anda ialah: Aries")
            else:
                print("Astrologi anda ialah: Taurus")
        else:
            print(f"Bulan April tidak memiliki tanggal {tanggal} !")
            print("Bulan ini hanya memiliki tanggal 1 - 30 saja")

    elif (bulan == 5 or bulan == daftar_bulan[4]):
        if (tanggal > 0 and tanggal <= 31):
            if (tanggal > 0 and tanggal < 21):
                print("Astrologi anda ialah: Taurus")
            else:
                print("Astrologi anda ialah: Gemini")
        else:
            print(f"Bulan Mei tidak memiliki tanggal {tanggal} !")
            print("Bulan ini hanya memiliki tanggal 1 - 31 saja")

    elif (bulan == 6 or bulan == daftar_bulan[5]):
        if (tanggal > 0 and tanggal <= 30):
            if (tanggal > 0 and tanggal < 21):
                print("Astrologi anda ialah: Gemini")
            else:
                print("Astrologi anda ialah: Cancer")
        else:
            print(f"Bulan Juni tidak memiliki tanggal {tanggal} !")
            print("Bulan ini hanya memiliki tanggal 1 - 30 saja")

    elif (bulan == 7 or bulan == daftar_bulan[6]):
        if (tanggal > 0 and tanggal <= 31):
            if (tanggal > 0 and tanggal < 23):
                print("Astrologi anda ialah: Cancer")
            else:
                print("Astrologi anda ialah: Leo")
        else:
            print(f"Bulan Juli tidak memiliki tanggal {tanggal} !")
            print("Bulan ini hanya memiliki tanggal 1 - 31 saja")

    elif (bulan == 8 or bulan == daftar_bulan[7]):
        if (tanggal > 0 and tanggal <= 31):
            if (tanggal > 0 and tanggal < 23):
                print("Astrologi anda ialah: Leo")
            else:
                print("Astrologi anda ialah: Virgo")
        else:
            print(f"Bulan Agustus tidak memiliki tanggal {tanggal} !")
            print("Bulan ini hanya memiliki tanggal 1 - 31 saja")

    elif (bulan == 9 or bulan == daftar_bulan[8]):
        if (tanggal > 0 and tanggal <= 30):
            if (tanggal > 0 and tanggal < 23):
                print("Astrologi anda ialah: Virgo")
            else:
                print("Astrologi anda ialah: Libra")
        else:
            print(f"Bulan September tidak memiliki tanggal {tanggal} !")
            print("Bulan ini hanya memiliki tanggal 1 - 30 saja")

    elif (bulan == 10 or bulan == daftar_bulan[9]):
        if (tanggal > 0 and tanggal <= 31):
            if (tanggal > 0 and tanggal < 23):
                print("Astrologi anda ialah: Libra")
            else:
                print("Astrologi anda ialah: Scorpio")
        else:
            print(f"Bulan Oktober tidak memiliki tanggal {tanggal} !")
            print("Bulan ini hanya memiliki tanggal 1 - 31 saja")

    elif (bulan == 11 or bulan == daftar_bulan[10]):
        if (tanggal > 0 and tanggal <= 30):
            if (tanggal > 0 and tanggal < 22):
                print("Astrologi anda ialah: Scorpio")
            else:
                print("Astrologi anda ialah: Sagittarius")
        else:
            print(f"Bulan November tidak memiliki tanggal {tanggal} !")
            print("Bulan ini hanya memiliki tanggal 1 - 30 saja")

    elif (bulan == 12 or bulan == daftar_bulan[11]):
        if (tanggal > 0 and tanggal <= 31):
            if (tanggal > 0 and tanggal < 22):
                print("Astrologi anda ialah: Sagittarius")
            else:
                print("Astrologi anda ialah: Capricorn")
        else:
            print(f"Bulan Desember tidak memiliki tanggal {tanggal} !")
            print("Bulan ini hanya memiliki tanggal 1 - 31 saja")



# >> Penyelesaian Program 4 <<
# Zodiak / Astrologi Cina
print("\n\n\nProgram 4: Zodiak / Astrologi Cina")
daftar_astrologi_cina = {
    'Ayam Jantan': 1981,
    'Anjing': 1982,
    'Babi': 1983,
    'Tikus': 1984,
    'Ox': 1985,
    'Macan': 1986,
    'Kelinci': 1987,
    'Naga': 1988,
    'Ular': 1989,
    'Kuda': 1990,
    'Kambing': 1991,
    'Monyet': 1992
}

tahun_lahir = 2009
print(f"Tahun lahir anda: {tahun_lahir}")


if (tahun_lahir == daftar_astrologi_cina["Ayam Jantan"] or ((tahun_lahir - 1981) % 12 == 0)):
    print("Astrologi Cina anda ialah: Ayam Jantan")
elif (tahun_lahir == daftar_astrologi_cina["Anjing"] or ((tahun_lahir - 1982) % 12 == 0)):
    print("Astrologi Cina anda ialah: Anjing")
elif (tahun_lahir == daftar_astrologi_cina["Babi"] or ((tahun_lahir - 1983) % 12 == 0)):
    print("Astrologi Cina anda ialah: Babi")
elif (tahun_lahir == daftar_astrologi_cina["Babi"] or ((tahun_lahir - 1984) % 12 == 0)):
    print("Astrologi Cina anda ialah: Babi")
elif (tahun_lahir == daftar_astrologi_cina["Tikus"] or ((tahun_lahir - 1985) % 12 == 0)):
    print("Astrologi Cina anda ialah: Tikus")
elif (tahun_lahir == daftar_astrologi_cina["Ox"] or ((tahun_lahir - 1986) % 12 == 0)):
    print("Astrologi Cina anda ialah: Ox")
elif (tahun_lahir == daftar_astrologi_cina["Macan"] or ((tahun_lahir - 1987) % 12 == 0)):
    print("Astrologi Cina anda ialah: Macan")
elif (tahun_lahir == daftar_astrologi_cina["Kelinci"] or ((tahun_lahir - 1988) % 12 == 0)):
    print("Astrologi Cina anda ialah: Kelinci")
elif (tahun_lahir == daftar_astrologi_cina["Naga"] or ((tahun_lahir - 1989) % 12 == 0)):
    print("Astrologi Cina anda ialah: Naga")
elif (tahun_lahir == daftar_astrologi_cina["Ular"] or ((tahun_lahir - 1990) % 12 == 0)):
    print("Astrologi Cina anda ialah: Ular")
elif (tahun_lahir == daftar_astrologi_cina["Kuda"] or ((tahun_lahir - 1991) % 12 == 0)):
    print("Astrologi Cina anda ialah: Kuda")
else:
    print("Astrologi Cina anda ialah: Monyet")