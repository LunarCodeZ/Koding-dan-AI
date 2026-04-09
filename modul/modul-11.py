# =============================
# MODUL 11 - OBJECT CLASS
# =============================





# === Latihan ===
print("=== Latihan ===\n")
'''
Buatlah:
(1) Membuat detail personal menggunakan object dan class
(2) Mengubah soal program di modul 10 (a, b, c, d) menjadi object dan class
'''



# Penyelesaian Program 1
# Detail personal dengan object dan class
print("- Program 1: Detail personal dengan object dan class -")
# Class for Computer Science Student  
class Person:  
    # Class Variable  
    person = 'Person'             

    # The init method or constructor  
    def __init__(self, rambut, warna):  
        # Instance Variable      
        self.rambut = rambut
        self.warna = warna
        
# Objects 
Budi = Person("Ikal", "Hitam")  
Michael = Person("Lurus", "Pirang") 

print('Budi details:')      
print('Rambut: ', Budi.rambut) 
print('Warna Rambut: ', Budi.warna) 

print('\nMichael details:')      
print('Rambut: ', Michael.rambut)
print('Warna Rambut: ', Michael.warna)
      


# Penyelesaian Program 2
# Mengubah soal di modul 10 menjadi object dan class
print("\n\n- Program 2: Mengubah soal di modul 10 menjadi object dan class -")

class Modul10:
    def hitungFaktorial():
        print("\nA.) Nilai faktorial angka masukan")
        angka_faktorial = int(input("Masukkan angka yang akan di faktorialkan: "))
        for faktor in range(angka_faktorial + 1):
            if (faktor < 1):
                hasil_faktor = 1
            else:
                hasil_faktor *= faktor
        print(f"Hasil faktorisasi: {hasil_faktor}")


    def hitungKarakter():
        print("\nB.) Hitung karakter string uppercase dan lowercase")
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVSXYZ"
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        kalimat = str(input("Ketikkan sebuah kalimat: "))
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


    def segitigaPascal():
        print("\n\C.) Segitiga pascal dari angka masukan")
        angka_segitiga = int(input("Masukkan angka: "))
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


    def angkaPerkalian():
        print("\nD.) List angka yang dikali angka sendiri")
        awal_range = int(input("Masukkan awal range: "))
        akhir_angka_sebelum = int(input("Masukkan akhir angka sebelum: "))
        hasil_list_angka = []

        for i in range(awal_range, akhir_angka_sebelum):
            hasil_list_angka.append(i * i)
        print(f"Hasil: {hasil_list_angka}")




modul_10 = Modul10()
modul_10.hitungFaktorial()
modul_10.hitungKarakter()
modul_10.segitigaPascal()
modul_10.angkaPerkalian()