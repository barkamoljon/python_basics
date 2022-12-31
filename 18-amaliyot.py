#1
buyurtmalar =[]
print("Buyurtma qabul qiluvchi dastur")
n=1
while True:
     savol = f"{n}-buyurtmangizni kiriting:"
     buyurtma = input(savol)
     buyurtmalar.append(buyurtma)
     javob = input("Yana buyurtma qo`shasizmi?(ha/yo`q)")
     if javob =='ha':
       n+1
       continue
     else:
       break
#2 
print("Onlayn bozorga mahsulotlar qo`shuvchi dastur.")
mahsulotlar = {}
ishora = True
while ishora:
    mahsulot = input("E-bozorga mahsulot kiriting ")
    narx = input(f"{mahsulot.title()} narxini kiriting: ")
    mahsulot[mahsulot] = int(narx)

    javob = input("Yana buyurtma qo`shasizmi?(ha/yo`q)")
    if javob == 'yo`q':
      ishora = False
#3
#Berilgan mahsulotlar orqali qilish mumkin, agar hohlasa tayyor qiymatlardan foydalanish mumkin.
#Mening javobim 
ishora = True
while ishora:
    for mahsulot,narx in mahsulotlar.items():
        if mahsulot in buyurtmalar: 
            print(f"{mahsulot.title()}-{narx} so`m")
        else:
            print(f"Bizda {mahsulot} yo'q")
            ishora=False
#Ustozning javoblari
buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")
