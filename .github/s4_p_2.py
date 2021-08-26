Riazi1 = ['ali', 'mmd','reza','maryam','nader','reza']
Fizik1 = ['ali','mmd', 'negar','fateme','mehrsa','nazi']
kol1 = Fizik1+Riazi1
tedad = len(kol1)
my_set1 = set(Fizik1)
my_set2 = set(Riazi1)
eshterek = my_set1.intersection(my_set2)

print(f'ajzaye kol 2 kelas {kol1}ast va {tedad} nafar hatand')
print(f'eshtrak 2 kelas {eshterek} hastand ke dar 2 kelas sherkat kardn')

