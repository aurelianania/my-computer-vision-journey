#Buat sebuah program yang menghitung frekuensi kemunculan kata dalam sebuah teks pendek (string).
#Simpan hasilnya dalam bentuk Dictionary { "kata": jumlah_kemunculan }
def hitung_kata(teks):
    frekuensi={}

    kumpulan_kata= teks.split()

    for kata in kumpulan_kata:
        kata_bersih= kata.lower()

        if kata_bersih in frekuensi:
            frekuensi[kata_bersih] += 1
        
        else:
            frekuensi[kata_bersih] = 1
    
    return frekuensi

kalimat_contoh= "Piksel gambar itu berwarna merah dan piksel ini berwarna biru"
hasil_hitung= hitung_kata(kalimat_contoh)

print(hasil_hitung)
