#1
x = int(input("Juft son kiriting: "))
print("Raxmat") if x%2==0 else print("Bu son juft emas")
#2
yosh = int(input('Yoshingizni kiriting: '))
if yosh<4 or yosh>60:
  price = 0
elif x<18:
  price = 10000
else:
  price = 20000  
print(f"Sizga chipta narxi {price} so`m")
#3
print('Ikkita son kiriting: ')
x = float(input('Birinchi sonni kirirting: '))
y = float(input('Ikkinchi sonni kirirting: '))
if x==y :
  print(f'{x}={y}')
elif x>y:
  print(f'{x}>{y}')
else :
  print(f'{x}<{y}')
#4
mahsulotlar = ['olma','pichloq','qovun','tarvuz','piyoz','kartoshka', 'pomidor','baqlajon','holva','savzi']
savat = []
print("Kamida beshta mahsulot kiriting")
for n in range(5): 
  savat.append(input(f"{n+1}-mahsulot kirirting: "))
for mahsulot in savat:#demak birinchi berilgan qiymatlardan har birini oladi 
    if mahsulot in mahsulotlar:#So`ngra  bor mahsulotlar bilan har birirni tekshirib ko`radi.
       print(f"{mahsulot} do'konimizda bor")
    else:
       print(f"{mahsulot} do'konimizda yo'q")
#6
mahsulotlar = ['olma','pichloq','qovun','tarvuz','piyoz','kartoshka', 'pomidor','baqlajon','holva','savzi']
savat = []
bor_mahsulotlar =[]
mavjud_emas = []
print("Kamida beshta mahsulot kiriting")
for n in range(5): 
  savat.append(input(f"{n+1}-mahsulot kirirting: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
       bor_mahsulotlar.append(mahsulot)
    else:
       mavjud_emas.append(mahsulot)
if not mavjud_emas:
  print(f"Siz so'ragan barcha mahsulotlar do'konimizda bor")
else:
  print(f"Quyidagi mahsulotlar do`konimizda yo`q:{mavjud_emas}")
#7
foydalanuvchi = ['osiyo','maryam','abdulloh','abdurahmon','muhammad']
yangi_login = input("Yangi login kiriting: ")
if yangi_login.lower() in foydalanuvchi:
  print("Login band, yangi login tanlang!")
else:
  print(f"Xush kelibsiz, {yangi_login}!")
#8
butun_son = int(input("Biror butun son kiriting: "))
for n in range(2,11):
  if butun_son%n==0:
    #print(f"Qolsiqsiz bo`linuvchi sonlar:{n} ")
    print(f"{butun_son} soni {n} ga qoldiqsiz bo'linadi")
