Riazi1 = ('ali', 'mmd','reza','maryam','nader','reza')
Fizik1 = ('ali','mmd', 'negar','fateme','mehrsa','nazi')
my_set1 = set(Riazi1)
my_set2 = set(Fizik1)
kol1 = Fizik1+Riazi1
tedad = len(kol1)
m = set(kol1)
eshterek = my_set2.intersection(my_set1)

print(f'ajzaye kol 2 kelas {kol1}ast va {tedad} nafar hatand')
print(f'eshtrak 2 kelas {eshterek} hastand ke dar 2 kelas sherkat kardn')
new = m - eshterek
print(new)

