import modulAritmatika

bil1 = input("masukkan angka pertama : ")
bil2 = input("masukkan angka kedua : ")
pilih = input("pilih operasi aritmatika : ")

print()

if pilih == "tambah":
    print(modulAritmatika.tambah(bil1, bil2))
elif pilih == "kurang":
    print(modulAritmatika.kurang(bil1, bil2))
else :
    print(modulAritmatika.kali(bil1, bil2))

print()
print("terimakasih silahkan mengulang kembali")