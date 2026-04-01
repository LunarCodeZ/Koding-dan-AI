# ==============================
# MODUL 9 - TUPLE DAN DICTIONARY
# ==============================





# === Latihan ===
print("=== Latihan ===\n")
'''
Buatlah:
(1) Program menampilkan isi dari tuple
    lalu konversi ke format string
(2) Program menampilkan penjumlahan bilangan
    yang ada pada dictionary
(3) Program menampilkan hasil perkalian dari
    setiap dictionary yang ada
(4) Program menghapus key pada dictionary dan menampilkan
    perbedaan antara dictionary pertama dan dictionary
    kedua yang sudah berubah
(5) Program permainan binatang dalam bahasa inggris
    ke bahasa Indonesia
'''



# >> Penyelesaian Program 1 <<
# Program yang menampilkan isi dari tuple
# lalu konversi ke format string
print("- Program 1: Menampilkan isi tuple lalu konversi ke format string -")
tupel_1 = ('I', 'n', 'f', 'i', 'n', 'i', 't', 'e')

print(f"Isi tuple: {tupel_1}")
print(f"Konversi ke format string: {''.join(tupel_1)}")



# >> Penyelesaian Program 2 <<
# Program yang menampilkan penjumlahan bilangan
# yang ada pada dictionary
print("\n\n- Program 2: Menampilkan penjumlahan bilangan pada dictionary -")
dictionary_penjumlahan = {
    'bilangan_1': 90,
    'bilangan_2': -54,
    'bilangan_3': 0.4
}

print(f"Bilangan pada dictionary: {dictionary_penjumlahan}")

for bilangan in dictionary_penjumlahan.values():
    if (bilangan == dictionary_penjumlahan['bilangan_1']):
        hasil_penjumlahan = bilangan
    else:
        hasil_penjumlahan += bilangan

print(f"Hasil penjumlahan: {hasil_penjumlahan}")



# >> Penyelesaian Program 3 <<
# Program yang menampilkan hasil perkalian dari
# setiap dictionary yang ada
print("\n\n- Program 3: Menampilkan hasil perkalian dari setiap dictionary yang ada -")
perkalian = int(input("Masukkan angka: "))
keys_perkalian = []
values_perkalian = []

for bilangan_perkalian in range(perkalian + 1):
    if (bilangan_perkalian < 1):
        pass
    else:
        keys_perkalian.append(bilangan_perkalian)
        values_perkalian.append(bilangan_perkalian * bilangan_perkalian)

dictionary_perkalian = dict.fromkeys(keys_perkalian, 0)

for angka_perkalian in range(len(dictionary_perkalian) + 1):
    if (angka_perkalian < 1):
        pass
    else:
        dictionary_perkalian[angka_perkalian] = angka_perkalian * angka_perkalian

print(f"Hasil perkalian dictionary: {dictionary_perkalian}")



# >> Penyelesaian Program 4 <<
# Program yang menghapus key pada dictionary dan menampilkan
# perbedaan antara dictionary pertama dan dictionary
# kedua yang sudah berubah
print("\n\n- Program 4: Menghapus key pada dictionary dan menampilkan perbedaannya -")
dictionary_a = {
    'nis': 11524,
    'nama': "Erik Yanuar Putra",
    'umur': 16,
    'hobi': ["Coding", "Bermain game"],
    'cita-cita': "Game / Application Developer"
}
dictionary_b = dict.copy(dictionary_a)

print("Dictionary original: \n{")
for dict_a in dictionary_a:
    print(f"{dict_a}: {dictionary_a[dict_a]}")
print("}")

dictionary_b.pop('cita-cita')
print("\nDictionary setelah dihapus: \n{")
for dict_b in dictionary_b:
    print(f"{dict_b}: {dictionary_b[dict_b]}")
print("}")

# Menampilkan perbedaan dictionary
print("\nPerbedaan kedua dictionary:")
for perbedaan in dictionary_a:
    if (perbedaan in dictionary_b):
        print(f"'{perbedaan}' ada di dictionary_b")
    else:
        print(f"'{perbedaan}' tidak ada di dictionary_b !")



# >> Penyelesaian Program 5 <<
# Program permainan tebak nama binatang dalam bahasa inggris
# ke bahasa Indonesia
print("\n\n- Program 5: Permainan tebak nama binatang dalam bahasa Inggris ke bahasa Indonesia -")
dictionary_binatang = {
    "Ant": "Semut",
    "Bee": "Lebah",
    "Mosquito": "Nyamuk",
    "Butterfly": "Kupu-kupu",
    "Spider": "Laba-laba",
    "Fly": "Lalat",
    "Hedgehog": "Landak",
    "Snail": "Siput"
}

print("=== Game Tebak Binatang dalam Bahasa Inggris === \n")
aksi = str(input("Mau bermain ? (y/n): "))

match aksi:
    case "y" | "Y":
        for pertanyaan in dictionary_binatang:
            print(f"{pertanyaan} ?")
            jawaban = str(input("Jawaban Anda: "))

            print(f"{dictionary_binatang[pertanyaan]} \n")
            if (jawaban == dictionary_binatang[pertanyaan]):
                print("BENAR !")
            else:
                print("SALAH...")

            print("______________________________________")
        print("\nTerimakasih sudah bermain :)")

    case "n" | "N":
        print("Baiklah kalau begitu...")

    case _:
        print("Mohon ulangi lagi...")