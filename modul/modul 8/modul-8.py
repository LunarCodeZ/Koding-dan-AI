# =============================
# MODUL 8 - LIST
# =============================





# === Latihan ===
print("=== Latihan ===\n")
'''
Buatlah:
(1) Program yang menampilkan nilai maksimum dari sebuah list
(2) Program yang menampilkan nilai minimum dari sebuah list
(3) Program yang menampilkan kata yang tidak boleh lebih dari 4 huruf
(4) Program yang menampilkan sebuah anggota baru di antara setiap
    anggota list
(5) Program decrypt dari modul 7 dengan menggunakan caesar cipher
'''



# >> Penyelesaian Program 1 <<
# Program yang menampilkan nilai maksimum dari sebuah list
print("- Program 1: Menampilkan nilai maksimum dari sebuah list -")
nilai_siswa = [85, 90, 40, 33, 95, 93]

print(f"List: {nilai_siswa}")
print(f"Nilai Maksimum (terbesar): {max(nilai_siswa)}")



# >> Penyelesaian Program 2 <<
# Program yang menampilkan nilai minimum dari sebuah list
print("\n\n- Program 2: Menampilkan nilai minimum dari sebuah list -")
print(f"List: {nilai_siswa}")
print(f"Nilai Minimum (terkecil): {min(nilai_siswa)}")



# >> Penyelesaian Program 3 <<
# Program yang menampilkan kata yang tidak boleh lebih dari 4 huruf
print("\n\n- Program 3: Menampilkan kata yang tidak boleh lebih dari 4 huruf -")
kalimat = "Hari ini saya, Erik Yanuar Putra akan mempelajari tentang bahasa pemrograman Python"
print(f"Kalimat: {kalimat}")

simbol_skip = [',', '.', '/', '|', '?', '!']
kata_4_huruf = []
kumpulan_kata = []
penghitung_angka = 0

for kata in range(len(kalimat)):
    if (kalimat[kata] == " " or kalimat[kata] in simbol_skip):
        if (penghitung_angka > 4):
            kata_4_huruf.append(''.join(kumpulan_kata))
        else:
            pass
        kumpulan_kata = []
        penghitung_angka = 0
        
    elif (kata == len(kalimat) - 1):
        kumpulan_kata.append(kalimat[kata])
        penghitung_angka += 1
        if (penghitung_angka > 4):
            kata_4_huruf.append(''.join(kumpulan_kata))
        else:
            pass
        kumpulan_kata = []
        penghitung_angka = 0
        print(f"Kata yang lebih dari 4 huruf: {', '.join(kata_4_huruf)}")
    
    else:
        kumpulan_kata.append(kalimat[kata])
        penghitung_angka += 1



# >> Penyelesaian Program 4 <<
# Program yang menampilkan sebuah anggota baru di antara setiap anggota list
print("\n\n- Program 4: Memasukkan anggota baru di sela-sela anggota list -")
list_asli = ["Rusa", "Buaya", "Kucing", "Elang", "Bebek"]
anggota_baru = "a"
list_akhir = []
print(f"List original: {list_asli}")
print(f"Anggota yang akan ditambahkan: {anggota_baru}")

for anggota in list_asli:
    list_akhir.append(anggota)
    list_akhir.append(anggota_baru)
print(f"Hasil akhir: {list_akhir}")




# >> Penyelesaian Program 5 <<
# Program decrypt dari modul 7 dengan menggunakan caesar cipher
print("\n\n- Program 5: Dekripsi caesar cipher -")
daftar_huruf = "abcdefghijklmnopqrstuvwxyz"
daftar_huruf_upper = daftar_huruf.upper()

kalimat_enkripsi = "jxd vxnd glddd"
langkah = 3
langkah %= 26
hasil_dekripsi = ""

for huruf in kalimat_enkripsi:
    if (huruf != " "):
        if (daftar_huruf.index(huruf) - langkah > 25):
            hasil_dekripsi += daftar_huruf[(daftar_huruf.index(huruf) + langkah) % 26]
        else:
            hasil_dekripsi += daftar_huruf[daftar_huruf.index(huruf) - langkah]
    else:
        hasil_dekripsi += " "

print(f"Hasil dekripsi: {hasil_dekripsi}")