#1
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] 
for car in cars:
  if car == 'gm':
    print(car.upper())
  else:
    print(car.title())
#2
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] 
for car in cars:
  if car != 'gm':
    print(car.title())
  else:
    print(car.upper())
#3
foydalanuvchi_ismi = input('Ismingizni kiriting:\n>>> ')
if foydalanuvchi_ismi == 'Admin':
  print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
  print(f"Xush kelibsiz, {foydalanuvchi_ismi}!")
#4
print('Ikkita son kiriting: ')
x = float(input('Birinchi sonni kirirting: '))
y = float(input('Ikkinchi sonni kirirting: '))
if x==y :
  print('Sonlar teng')
#5
x = float(input('Istalgan sonni kirirting: '))
print("Musbat son") if x>=0 else  print('Manfiy son')
#6
x = float(input('Son kirirting: '))
print(f"{x**0.5}") if x>0 else print("Musbat son kiriting")
