#1
ismlar = ['Barkamol','Jalol','Jamol','Ali','Hamid']
for ism in ismlar:
  print(f'Assalomu Alaykum va Rohmatullohi va Barokatuh {ism}')
#2
print("Kod", len(ism), 'marta takrorlandi')
#3
toq_sonlar = list(range(11,100))
for toq in toq_sonlar:
  print(f'{toq**3}')
 #4
kinolar = []
print("5 ta eng yaxshi ko`rgan kinolar no mini kiriting: ")
for n in range(5):
 kinolar.append(input(f'{n+1}-kinoyingizni nomini kiriting: '))
print(kinolar) 
#6
odamlar = []
n_insonlar = int(input("Bugun necha kishi bilan suhbatlashdingiz?\n>>>:"))
for n in range(n_insonlar):
  odamlar.append(input(f'Bugun suhbatlashgan {n+1}-insoningizni ismi: '))
print(odamlar)
