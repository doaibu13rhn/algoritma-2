class Pembayaran:
    def bayar(self):
        print("Melakukan pembayaran")


class Tunai(Pembayaran):
    def bayar(self):
        print("Pembayaran dilakukan secara tunai")


class Transfer(Pembayaran):
    def bayar(self):
        print("Pembayaran dilakukan melalui transfer")


# Membuat objek
pembayaran1 = Tunai()
pembayaran2 = Transfer()

# Polimorfisme
pembayaran1.bayar()
pembayaran2.bayar()