#Buat sebuah fungsi yang menerima list berisi angka acak.
#Fungsi tersebut harus mengembalikan list baru yang HANYA berisi angka genap,
#dan angka genap tersebut harus dikalikan dua.
def proses_angka_genap(daftar_angka):
    hasil=[]

    for angka in daftar_angka:
        if angka % 2== 0:
            hasil.append(angka*2)
    return hasil

data_input= [1,2,3,4,5,6,7,8]
data_output= proses_angka_genap(data_input)

print("input: ", data_input)
print("output: ", data_output)
