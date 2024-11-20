class Produk:

    def init(self, nama, harga):
        self.nama = nama
        self.harga = harga
        self.stok = None

    def get_stok(self):
        print(self.stok)

    def _set_stok(self, stok): 
        if stok > 0:
            self.stok = stok
        else: self.stok = "Habis"

class Pulsa (Produk):

    def set_stok(self, stok):

        if stok == "yes": 
            self.stok = "Tersedia"

        else: 
            self.stok = "N/A"

pulsa = Pulsa('Gopay', 100000) 
pulsa.set_stok("yes")
pulsa.get_stok()