# =============================
# MODUL 7 - NUMBER DAN STRING
# =============================





# === Latihan ===
print("=== Latihan ===\n")
'''
Buatlah program:
(1) String arrays: menampilkan karakter pada indeks ke-2,
    4, 8, 10 dari tipe data string
(2) String range (slicing): menampilkan karakter pada
    indeks ke 1-3, 2-5, dan 7-11
(3) Mengubah kalimat yang diketik menjadi lowercase dan
    uppercase lalu menampilkan hasilnya
(4) Enkripsi caesar cipher
'''



# >> Penyelesaian Program 1 <<
# String arrays
print("Program 1: String arrays")
kalimat = "Halo semuanya"

print(f"Kalimat: {kalimat}")
print(f"Karakter indeks ke-2: {kalimat[2]}") # --> Menampilkan karakter ke 3 dari kalimat
print(f"Karakter indeks ke-4: {kalimat[4]}") # --> Menampilkan karakter ke 5 dari kalimat
print(f"Karakter indeks ke-8: {kalimat[8]}") # --> Menampilkan karakter ke 9 dari kalimat
print(f"Karakter indeks ke-10: {kalimat[10]}") # --> Menampilkan karakter ke 11 dari kalimat



# >> Penyelesaian Program 2 <<
# String range
print("\n\nProgram 2: String range")
kalimat_range = "Halo semuanya"

print(f"Kalimat: {kalimat_range}")
print(f"Karakter dari indeks 1-3: {kalimat_range[1:3]}")
print(f"Karakter dari indeks 2-5: {kalimat_range[2:5]}")
print(f"Karakter dari indeks 7-11: {kalimat_range[7:11]}")



# >> Penyelesaian Program 3 <<
# Mengubah kalimat menjadi lowercase dan uppercase
print("\n\nProgram 3: Mengubah kalimat menjadi lowercase dan lowercase")
daftar_huruf = "abcdefghijklmnopqrstuvwxyz"
daftar_huruf_upper = daftar_huruf.upper()

kalimat_asli = "Halo Semuanya, aku AGUS"
kalimat_asli2 = "orang jahat adalah orang baik yang tersakiti"
hasil_perubahan = ""

print(f"Kalimat: {kalimat_asli}")
print(f"Kalimat lowercase: {kalimat_asli.lower()}")
print(f"Kalimat uppercase: {kalimat_asli.upper()}")
for huruf in kalimat_asli2:
    if (huruf == 'a' or huruf == 'o' or huruf == 'e'):
        hasil_perubahan += "i"
    else:
        hasil_perubahan += huruf
print(f"Kalimat asli: {kalimat_asli2}")
print(f"Setelah a, o, dan e diubah menjadi i: {hasil_perubahan}")



# >> Penyelesaian Program 4 <<
# Enkripsi caesar cipher
print("\n\n- Program 4: Enkripsi caesar cipher -")

string_original = str(input("Masukkan string: "))
langkah = int(input("Masukkan berapa langkah: "))
langkah %= 26

print(f"Kalimat original: {string_original}")
print(f"Langkah: {langkah}")

hasil_enkripsi = ""
for huruf in string_original:
    if (huruf != " "):
        if (daftar_huruf.index(huruf) + langkah > 25):
            hasil_enkripsi += daftar_huruf[(daftar_huruf.index(huruf) + langkah) % 26]
        else:
            hasil_enkripsi += daftar_huruf[daftar_huruf.index(huruf) + 2]
    else:
        hasil_enkripsi += " "   
    

print(hasil_enkripsi)