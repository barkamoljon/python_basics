def foydalanuvchi_info(ismi,familiyasi,t_yili,t_joyi,email='',telefon=''):
  """Foydalanuvchi haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
  foydalanuvchi= {'ism':ismi,
                   'familiya':familiyasi,
                   't_yil':t_yili,
                   't_joy':t_joyi,
                   'email':email,
                   'telefon':telefon}
  return foydalanuvchi 
#2
def foydalanuvchi_kirit():
  """Foydalanuvchiga foydalanuvchi_info funksiyasi yordamida bir nechta foydalanuvchilar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
  print("Saytimizdagi foydalanuvchi royxatini shakllantiramiz. ")
  foydalanuvchilar = []
  while True:
    print("\nQuyidagi ma`lumotlarni kiriting",  end='')
    ismi=input("Ismingizni kiriting: ")
    familiyasi=input("Familyangizni kiriting: ")
    t_yili=int(input("Tug`ilgan yilingizni kiriting: "))
    t_joyi=input("Tug`ilgan joyingizni kiriting: ")
    email=input("Elektron pochtangizni kiriting: ")
    telefon=input("Telefon raqamingizni kiriting: ")
    foydalanuvchilar.append(foydalanuvchi_info(ismi,familiyasi,t_yili,t_joyi,email,telefon))
    print('Ro`yhatimizdagi foydalanuvchilar:')
    for foydalanuvchi in foydalanuvchilar:
      if foydalanuvchi['email']:
          email = foydalanuvchi['email']
      else:
          email = "No'malum"
      if foydalanuvchi['telefon']:
        telefon = foydalanuvchi ['telefon']
      else:
        telefon = "No'malum"
    javob = input("Yana foydalanuvchi qo'shasizmi? (yes/no): ")
    if javob=='no':
        break
    return foydalanuvchilar

def info_print(avto_info):
    """Foydalanuvchilar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{foydalanuvchi_info['ism'].title()} {foydalanuvchi_info['familiya'].title()} "
          f"{foydalanuvchi_info['t_joy'].title()}da, {foydalanuvchi_info['t_yil']}-yil tug`ilgan, "
          f"Email pochtasi:{email}, Telfon raqami:{telefon}")

#Modul holatiga keldi,bularni biror faylga joylab unga nom bersak, shu nom orqali bu modulni chaqirsak bo`ladi
#quyidagi singari
#import avto_info_mod # avto_info_mod faylini (modulini) chaqiramiz

#avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
#avto_info_mod.info_print(avto1)

#Python modullari
#math moduli
import math
#1)
x=900
print(math.sqrt(x))# ildiz
#2)
print(power(2,10))#daraja
from math import pi # pi ning qiymati
r=5
l=pi*r**2
print(l)
#3
print(math.log3(9))
print(math.log10(100))
#random moduli
#randint
import random as r

son = r.randint(1,1000)
print(son)
#choice(x)
ismlar = ['olim','anvar','hasan','husan']
ism = r.choice(ismlar)
print(ism)
print(r.choice(ism))

x=list(range(43))
print(x)
print(r.choice(x))

#shuffle
x = list(range(40))
print(x)
r.shuffle(x)
print(x)
