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
print("\n\n\nProgram 2: String range")
kalimat_range = "Halo semuanya"

print(f"Kalimat: {kalimat_range}")
print(f"Karakter dari indeks 1-3: {kalimat_range[1:3]}")
print(f"Karakter dari indeks 2-5: {kalimat_range[2:5]}")
print(f"Karakter dari indeks 7-11: {kalimat_range[7:11]}")



# >> Penyelesaian Program 3 <<
# Mengubah kalimat menjadi lowercase dan uppercase
print("\n\n\nProgram 3: Mengubah kalimat menjadi lowercase dan lowercase")
kalimat_asli = "Halo Semuanya, aku AGUS"

print(f"Kalimat: {kalimat_asli}")
print(f"Kalimat lowercase: {kalimat_asli.lower()}")
print(f"Kalimat uppercase: {kalimat_asli.upper()}")



# >> Penyelesaian Program 4 <<
# Enkripsi caesar cipher
print("\n\n\nProgram 4: Enkripsi caesar cipher")
daftar_huruf = "abcdefghijklmnopqrstuvwxyz"
daftar_huruf_upper = daftar_huruf.upper()
kumpulan_huruf = []
kumpulan_kata = []

string_original = "sidoarjo kota yang maju"
langkah = 2
encrypt_counter = 1

print(f"Kalimat Original: {string_original}")
print(len(string_original))

# for huruf in string_original:
#     if (huruf == " "):
#         kumpulan_kata.append(''.join(kumpulan_huruf))
#         kumpulan_huruf = []
#     elif (huruf == string_original[-1]):
#         kumpulan_huruf.append(huruf)
#         kumpulan_kata.append(''.join(kumpulan_huruf))
#         kumpulan_huruf = []
#         print(' '.join(kumpulan_kata))
#     else:
#         kumpulan_huruf.append(huruf)

for huruf in string_original:
    huruf_counter = 0

    if (huruf == " "):
        kumpulan_kata.append(''.join(kumpulan_huruf))
        print(kumpulan_kata)
        kumpulan_huruf = []
        continue
        
    else:
        while (huruf_counter < len(daftar_huruf)):
            if (daftar_huruf[huruf_counter] == huruf):
                kumpulan_huruf.append(daftar_huruf[huruf_counter + langkah])
                break
            else:
                huruf_counter+=1
    
    encrypt_counter+=1