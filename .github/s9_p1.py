class Car():
    def __init__(self, brand, model, motor_volume, rang, curent_speed):
        self.brand = brand
        self.model = model
        self.motor_volume = motor_volume
        self.rang =rang
        self.curent_speed = curent_speed
    def __str__(self):
        return f'this is a {self.brand} {self.model} with {self.motor_volume} engine , with  {self.rang} colour'
    def boogh(self,boogh_lengh):
        boogh_lengh= 'b'+ 'o'*boogh_lengh +'gh'
        print(boogh_lengh)
    def noor_bala(self):
        print('noor bala')
    def gaz(self):
        self.curent_speed += 20
        print(f'soraat man {self.curent_speed} ast')

mybmw = Car('bmw', 'm8',1.5,'black',0)
mybmw.gaz()
mybmw.gaz()

