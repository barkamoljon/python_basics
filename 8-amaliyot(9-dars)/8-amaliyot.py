#1
davlatlar = ['Argentina','Braziliya','Saudiya Arabistoni','Misr','O`zbekiston']
print(davlatlar)
#2
print(len(davlatlar))
#3
print(sorted(davlatlar))
#4
print(sorted(davlatlar,reverse = True))
#5
print(davlatlar)
#6
print(davlatlar.reverse())
#7
print(davlatlar.sort())
print(davlatlar.sort(reverse = True))
#8
sonlar = list(range(120,1200,2))
#9
sum(sonlar)
#10
print(max(sonlar)-min(sonlar))
#11
print(len(sonlar))
#12
sonlar[:20]
sonlar[-20:]
sonlar[530:550]
#13
taomlar = ['pishloq','sariqyog`','osh','sho`rva','lag`mon']
#14
nonushta = taomlar[:]
#15
del nonushta [2:]
nonushta.insert(1,'murabbo')
#16
print(nonushta)
print(taomlar)
#QUyidagi mashqni ishlatish uchun '#' olib tashlang
#17
#nonushta = tuple(nonushta)
#nonushta[0] = 'qaymoq va non'
