class Car():
    def __init__(self, brand, model, motor_volume):
        self.brand = brand
        self.model = model
        self.motor_volume = motor_volume
    def boogh(self,boogh_lengh):
        boogh_lengh= 'b'+ 'o'*boogh_lengh +'gh'
        print(boogh_lengh)
    def noor_bala(self):
        print('noor bala')
print(Car.boogh(5))
