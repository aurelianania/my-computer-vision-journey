#Buatlah sebuah Class bernama ImageDatasetManager. Class ini harus bisa:
#1. Menyimpan daftar metadata gambar. Setiap gambar memiliki metadata berupa: filename (string), resolution (tuple: width, height), dan labels (list of strings, misal: ['cat', 'indoor']).
#2. Memiliki method untuk menambahkan gambar baru ke dalam dataset.
#3. Memiliki method untuk memfilter dan menampilkan gambar apa saja yang memiliki label tertentu (misal: cari semua gambar yang ada label 'cat').
#4. Memiliki method untuk menghitung rata-rata resolusi (width dan height) dari seluruh gambar yang ada di dataset.

class ImageDatasetManager:
    def __init__(self):
        self.dataset=[]
    
    def add_image(self, filename, resolution, labels):
        image_metadata= {
            "filename": filename,
            "resolution": resolution,
            "labels": labels
        }
        self.dataset.append(image_metadata)
        print(f"Berhasil menambahkan: {filename}")
    
    def filter_by_label(self, target_label):
        hasil_filter= []
        for img in self.dataset:
            if target_label in img["labels"]:
                hasil_filter.append(img["filename"])
        
        return hasil_filter
    
    def calculate_average_resolution(self):
        if not self.dataset:
            return 0,0
        
        total_width= 0
        total_height= 0

        for img in self.dataset:
            w, h = img["resolution"]
            total_width += w
            total_height += h
        
        jumlah_gambar= len(self.dataset)
        avg_width= total_width/jumlah_gambar
        avg_height= total_height/jumlah_gambar

        return avg_width, avg_height

manager= ImageDatasetManager()
manager.add_image("kucing_oren.jpg", (1920,1080), ["cat", "indoor", "animal"])
manager.add_image("mobil_balap.png", (1280,720), ["car", "outdoor", "speed"])
manager.add_image("anak_kucing.jpg", (640,480), ["cat", "cute"])

print("---")

gambar_kucing= manager.filter_by_label("cat")
print("Gambar dengan label 'cat': ", gambar_kucing)

rerata_w, rerata_h= manager.calculate_average_resolution()
print(f"Rata-rata resolusi dataset: {rerata_w} x {rerata_h} piksel")
