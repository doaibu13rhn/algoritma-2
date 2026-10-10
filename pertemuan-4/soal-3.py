class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def hitung_luas(self):
        return self.panjang * self.lebar
    
    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)



persegi = PersegiPanjang(15, 8)


print("Panjang         :", persegi.panjang)
print("Lebar           :", persegi.lebar)
print("Luas            :", persegi.hitung_luas())
print("Keliling        :", persegi.hitung_keliling())