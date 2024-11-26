from penjumlahan import jumlah
from pengurangan import kurang
from panjang_vektor import panjang
from sudut import sudut_antar_vektor
from dot_product import dot
from unit_vector import unit_vector

print("Operasi Pada Vektor 2D")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Panjang Vektor")
print("4. Sudut antara dua vektor")
print("5. Dot Product")
print("6. Unit Vector")

pilih = input("Pilih: ")

if pilih == '1':
    x1 = int(input("Komponen X untuk Vektor 1: "))
    y1 = int(input("Komponen Y untuk Vektor 1: "))
    x2 = int(input("Komponen X untuk Vektor 2: "))
    y2 = int(input("Komponen Y untuk Vektor 2: "))
    A = [x1, y1]
    B = [x2, y2]
    C = jumlah(A, B)
    print(f"{A} + {B} = {C}")

elif pilih == '2':
    x1 = int(input("Komponen X untuk Vektor 1: "))
    y1 = int(input("Komponen Y untuk Vektor 1: "))
    x2 = int(input("Komponen X untuk Vektor 2: "))
    y2 = int(input("Komponen Y untuk Vektor 2: "))
    A = [x1, y1]
    B = [x2, y2]
    C = kurang(A, B)
    print(f"{A} - {B} = {C}")

elif pilih == '3':
    x = int(input("Komponen X untuk Vektor: "))
    y = int(input("Komponen Y untuk Vektor: "))
    A = [x, y]
    result = panjang(A)
    print(f"Panjang vektor {A} adalah {result:.2f}")

elif pilih == '4':
    x1 = int(input("Komponen X untuk Vektor 1: "))
    y1 = int(input("Komponen Y untuk Vektor 1: "))
    x2 = int(input("Komponen X untuk Vektor 2: "))
    y2 = int(input("Komponen Y untuk Vektor 2: "))
    A = [x1, y1]
    B = [x2, y2]
    result = sudut_antar_vektor(A, B)
    print(f"Sudut antara vektor {A} dan {B} adalah {result:.2f} derajat")

elif pilih == '5':
    x1 = int(input("Komponen X untuk Vektor 1: "))
    y1 = int(input("Komponen Y untuk Vektor 1: "))
    x2 = int(input("Komponen X untuk Vektor 2: "))
    y2 = int(input("Komponen Y untuk Vektor 2: "))
    A = [x1, y1]
    B = [x2, y2]
    result = dot(A, B)
    print(f"Dot product dari {A} dan {B} adalah {result}")

elif pilih == '6':
    x = int(input("Komponen X untuk Vektor: "))
    y = int(input("Komponen Y untuk Vektor: "))
    A = [x, y]
    result = unit_vector(A)
    print(f"Unit vector dari {A} adalah {result}")

else:
    print("Pilihan tidak valid.")
