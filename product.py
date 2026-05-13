class Product:
    name: str
    price: float
    def show(this):
        print(this.name, this.price, ' TL' )

    # def __init__(self):
    #     self.name = ""
    #     self.price = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        


p1 = Product("Test 1",5)
p2 = Product("Test 2",10)

print(type(p1))
print(isinstance(p1,Product))

p1.name = "Küçük Prens"
p1.price = 250

p1.show()

p3 =Product('Başka bir kitap',300)
#p4= Product()

p3.show()