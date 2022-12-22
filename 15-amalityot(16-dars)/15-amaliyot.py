#1
python_izohli_lugati = {'integer':'butun son',
                 'float':'o`nlik son',
                 'if':"'agar' operatori",
                 'elif':"'aks holda,agar' operatori",
                 'else':"'aks holda' operatori",
                 'list':'bir o`zgaruvchiga bir nechta qiymatlarni salash imkonini beruvhi ma`lumot turi',
                 'tuple':'o`zgarmas ma`lumot turi',
                 'for ':'sikl nomi',
                 'variable':'o`zgaruvchi',
                 'lower':'barcha ma`lumotni kichik harfda taqdim qiladi'}
for k,q in sorted(python_izohli_lugati.items()):
  print(f"{k} - {q}") 
#2 
davlatlar = {'argentina':'buenes ayres',
             'braziliya':'braziliya',    
              'hindiston':'dehli',
              'germaniya':'berlin',
              'o`zbekiston':'toshkent'}

for davlat in sorted(davlatlar):
    print(f"{davlat.upper()} ")
    
for poytaxt in sorted(davlatlar.values()):
    print(f"{poytaxt.upper()} ")    
#3
davlat = input("Istalgan davlat nomini kiriting: ").lower()
print(davlatlar.get(davlat,"Bizda bunday ma'lumot yo'q").title())
#4
taomlar = {'osh':5000,
           'sho`rva':2000,
           'katlet':4000,
           'kabob':3000,
           'manti':2000,
           'so`msa':2000,
           'qozon kabob':7000,
           'lag`mon':6000,
           'chuchvara':4000,
           'golibsa':3500}
print("Kamida 3ta taom beyurma bering: ")    
buyurtma = []
for n in range(3):
  buyurtma.append(input(f"{n+1}-taomni kiriting: "))
for n in buyurtma:
  if n in taomlar:
    print(f"{n.title()} narxi {taomlar[n]} so`m")
  else:
    print(f'Bizda {n} yo`q')
