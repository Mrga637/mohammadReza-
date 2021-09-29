#------ Car
class Car():
    def __init__(self,brand, model,year):
        self.brand = brand
        self.model = model
        self.year = year
BMW = Car('BMW','M8', 2020)
Benz = Car('Mercedes-Benz', 'W202', 2004)
chevorlot = Car('Chevorlot', 'corut C8',2018)
print(BMW.model)
#------Mive
class Mive():
    def __init__(self,mive_esm, mive_rang, mive_maze):
        self.esm = mive_esm
        self.rang = mive_rang
        self.maze = mive_maze
hendone = Mive('Hendevane', 'daroon ghermez Biroon sabz', 'shirin')
moz = Mive('moz', 'zard', 'khosh taam')
print(hendone.maze)
#-----nooshidani
class nooshidani():
    def __init__(self,rang, ghelzat, maze, boo):
          self.rang = rang
          self.ghelzat = ghelzat
          self.maze = maze
          self.boo = boo
water = nooshidani('birang', 'raghigh', 'bi taam', 'bi boo')
coca = nooshidani('meshki', 'raghigh', 'shirin va ghazdar', 'booy bad nadre')
bear = nooshidani('zard', 'ham ghaliz ham raghigh', 'talkh', 'booye jo')
print(bear.maze)
#-----
