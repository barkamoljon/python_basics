#1
def yosh_hisobla(ism,yosh):
   """Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya."""
   print(f"{ism.title()} {2022-yosh} yilda tug`ilgan.")

#2
def darajaga_kotar(x):
  """Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya"""
  print(f'{x} ning kvadrati {x**2} ga, kubi {x**3} esa teng')
darajaga_kotar(5)
#3
def juftToqligi_top(x):
  """Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya"""
  if x%2==0:
    print(f'{x} juft son')
  else:
      print(f'{x} toq son')
#3
def taqqosla(x,y):
  """Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya"""
  if x>y:
    print(f"{x}>{y}") 
  elif x<y:
      print(f"{x}<{y}")
  else:
    print("Sonlar teng") 
taqqosla(5,9)
#4
def korsat(x,y):
  """Foydalanuvchidan x va y sonlarini olib, ularni konsolga chiqaruvchi funksiya"""
  print(f"x={x}\ny={y}")
korsat(5,10)
#5
def korsat(x,y=5):
  """Foydalanuvchidan x va y sonlarini olib, ularni konsolga chiqaruvchi funksiya"""
  print(f"x={x}\ny={y}")
#6
def qoldiqsiz_bol(x):
  """Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya"""
  for n in range(2,11):
    if x%n==0:
      print(f"{x}, {n} ga qoldiqsiz bo`inadi")
qoldiqsiz_bol(8)
juftToqligi_top(5)
