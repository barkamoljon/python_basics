#1
def kattalashtir(matnlar):
  '''Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya'''
  while matnlar:
    matn = matnlar.pop()
    k_matn = matn.capitalize()
    print(k_matn)
#Ustozning javoblari
def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()   

ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print(ismlar)
#2
hikmat_sozlari = ['men bugun yugurishga chiqmadim','xolamning qizi o`qishga kirdi','vaqt borida ilm ol, ilm olmoqchi bo`lganingda vaqt bo`lmasligi mumkin']
kattalashtir(hikmat_sozlari)
def buzmay_kattalashtir(matnlar):
  k_matnlar=[]
  for matn in matnlar:
    k_matn=matn.capitalize()   
    k_matnlar.append(k_matn)
  return k_matnlar
kattalashtir(hikmat_sozlari) 
#Ustozning javoblar
def katta_harf(matnlar):
    matnlar = matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()
    return matnlar

ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)
#3
def bahola(ismlar):
  baholar={ }
  while ismlar:
   for ism in ismlar:
      baho = int(input(f"Talaba {ism.title()}ning bahosini kirirting: "))
      baholar[ism]=baho
   return baholar
talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(talabalar)
#Alhamdulillah ustoz-shogirdan bir xil uslubda ishlanish, uslublar bir xil.
