#Konverte ppm
#Fungsi untuk menentukan massa bahan
#referensi website https://atlas-scientific.com/blog/what-is-parts-per-million-ppm/

def database_pelarut(bahan):
    #satuan g/ml didapatkan dari massa jenis
    #silahkan update database sesuai keinginan
    database = {
        "air":1,
        "ethanol":0.783,
        "peg":1.1
    }
    return database[bahan]

 # ========= Main Code ============
print("""
     =============== APLIKASI KONVERSI PPM =================
     = Author : Febri C                                    =
     = Lisensi : GPL                                       =
     = version : 1.1                                       =
     = Cara Penggunaan                                     =
     = Tinggal tulis bahannya, tanpa spasi, tanpa titik,   =
     = untuk memisahkan bahan pakai koma (,).              =
     = Masukan volume pelarut, gunakan koma, untuk         =
     = untuk memisahkan. Urutan harus sama dengan bahan    =
     = Masukan massa zat terlarut. Jadi deh                =
     =======================================================
     """)

bahan = input("Jenis Bahan Pelarut: ")
jumlah_pelarut = input("Jumlah Pelarut(ml): ")
massa_nanopartikel = float(input("Jumlah Nanopartikel (g): "))

input_bahan = bahan.split(",")
input_jumlah = jumlah_pelarut.split(",")

jumlah = 0

try:
    for index_inputbahan in range(len(input_bahan)):
        # print(database_pelarut(input_bahan[index_inputbahan])*float(input_jumlah[index_jumlah])) #debug
        jumlah += database_pelarut(input_bahan[index_inputbahan])*float(input_jumlah[index_inputbahan])

except KeyError:
    print("Ada Error: bahan pelarut tidak tersedia atau penulisan memakai spasi")

except ValueError:
    print("Ada Error: pada input angka jumlah pelarut atau massa nanopartikel")

print("Konsentrasi: ", round(massa_nanopartikel/jumlah*1000000,3), "ppm")
