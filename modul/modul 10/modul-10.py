# =============================
# MODUL 10 - FUNGSI FUNCTION
# =============================





# === Latihan ===
print("=== Latihan ===\n")
'''
Buatlah:
(1) Program menampilkan nilai faktorial dari
    angka yang di input
(2) Program menampilkan karakter dari string
    uppercase dan lowercase pada sebuah string
(3) Program menampilkan segitiga pascal dari
    angka yang dimasukkan
(4) Program yang menampilkan list angka
    yang dikalikan dengan angka itu sendiri 
'''



# >> Penyelesaian Program 1 <<
# Program yang menampilkan nilai faktorial
# dari angka yang di input
print("- Program 1: Nilai faktorial angka masukan -")
# angka = int(input("Masukkan angka yang akan difaktorialkan: "))
angka = 3
list_faktor = []

def faktorial(nilai_faktor):
    for faktor in range(nilai_faktor + 1):
        if (faktor < 1):
            hasil_faktor = 1
        else:
            hasil_faktor *= faktor

    print(f"Hasil faktorisasi: {hasil_faktor}")

faktorial(angka)



# >> Penyelesaian Program 2 <<
# Program yang menampilkan karakter dari string
# uppercase dan lowercase pada sebuah string
print("\n\n- Program 2: Karakter string uppercase dan lowercase -")
string_original = "Ani dan Budi sedang belajar di rumah Joko, di Desa Suka Maju"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVSXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"

def jumlahKarakter(kalimat):
    print(f"String original: {string_original}")
    jumlah_uppercase = 0
    jumlah_lowercase = 0

    for karakter in kalimat:
        if (karakter in uppercase):
            jumlah_uppercase += 1
        elif (karakter in lowercase):
            jumlah_lowercase += 1
        else:
            pass

    print(f"Jumlah karakter uppercase: {jumlah_uppercase}")
    print(f"Jumlah karakter lowercase: {jumlah_lowercase}")


jumlahKarakter(string_original)



# >> Penyelesaian Program 3 <<
# Program yang menampilkan segitiga pascal dari
# angka yang dimasukkan
print("\n\n- Program 3: Segitiga pascal dari angka masukan -")
angka_segitiga = int(input("Masukkan angka: "))

def segitigaPascal(n):
    pola_segitiga = []

    for i in range(n):
        baris = []
        for j in range(i + 1):
            if j == 0 or j == i:
                baris.append(1)
            else:
                baris.append(pola_segitiga[i-1][j-1] + pola_segitiga[i-1][j])
        pola_segitiga.append(baris)

    for row in range(len(pola_segitiga)):
        print(" ".join(map(str, pola_segitiga[row])))

segitigaPascal(angka_segitiga)



# >> Penyelesaian Program 4 <<
# Program yang menampilkan list angka
# yang dikalikan dengan angka itu sendiri 
print("\n\n- Program 4: List angka yang dikali angka sendiri -")
awal_range = int(input("Masukkan awal range: "))
akhir_angka_sebelum = int(input("Masukkan akhir angka sebelum: "))
hasil_list_angka = []

def listAngka(awal, akhir):
    for i in range(awal, akhir):
        hasil_list_angka.append(i * i)
    print(f"Hasil: {hasil_list_angka}")

listAngka(awal_range, akhir_angka_sebelum)