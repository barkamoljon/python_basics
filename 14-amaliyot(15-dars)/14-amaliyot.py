#1
ukam = {'ism':'Muhammad Aziz',
         'familiya': 'O`rinboyev',
         't_yil':2013,
         't_joy':'Toshkent Shahri'}

print(f"Mening ukamning ismi {ukam['ism']} {ukam['familiya']}.U {ukam['t_yil']}-yilda,{ukam['t_joy']}da tug`ilgan.")
#2
oila_azolar ={'otam':'Osh',
           "onam":'Manti',
           'ukam':'Pitsa',
           'katta_opam':'Katlet',
           'kichik_opam':'Lag`mon'} 
Osh = oila_azolar['otam']
Manti = oila_azolar['onam']
Pitsa = oila_azolar['ukam']
Katlet = oila_azolar['katta_opam']
print(f"Otamning sevimli taomi {Osh}, onamniki esa {Manti}, ukamniki {Pitsa}, katta opamniki bo`lsa {Katlet}")
#3
python_izohli_lugati = {'integer':'butun son',
                 'float':'o`nlik son',
                 'if':"for siklidagi 'agar' operatori",
                 'elif':"for siklidagi 'aks holda,agar' operatori",
                 'else':"for siklidagi 'aks holda' operatori",
                 'list':'bir o`zgaruvchiga bir nechta qiymatlarni salash imkonini beruvhi ma`lumot turi',
                 'tuple':'o`zgarmas ma`lumot turi',
                 'for ':'sikl nomi',
                 'variable':'o`zgaruvchi',
                 'lower':'barcha ma`lumotni kichik harfda taqdim qiladi'}
#4
#kalit = input("Kalit so`z kiriting: ").lower()
#print(python_izohli_lugati.get(kalit,'Bunday so`z mavjud emas'))
#5
kalit = input("Kalit so`z kiriting: ").lower()
tarijima = python_izohli_lugati.get(kalit)
if tarjima==None:
  print('Bunday so`z mavjud emas')
else: 
  print(f"{kalit.title()} so`zining ma`nosi {tarjima} degani")
