#Amaliy topshiriqlar
#1
def foydalanuvchi_info(ismi,familiyasi,t_yili,t_joyi,email='',telefon=''):
  foydalanuvchi= {'ism':ismi,
                   'familiya':familiyasi,
                   't_yil':t_yili,
                   't_joy':t_joyi,
                   'email':email,
                   'telefon':telefon}
  return foydalanuvchi 
#2
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
    print(f"{foydalanuvchi['ism']} {foydalanuvchi['familiya']}.{foydalanuvchi['t_joy']}da {foydalanuvchi['t_yil']}-yil tug`ilgan.Email pochtasi:{email}.Telefon raqami:{telefon}")   
  javob = input("Yana foydalanuvchi qo'shasizmi? (yes/no): ")
  if javob=='no':
        break
#3
def kattasini_top(a,b,c):
  """Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya """
  sonlar = max(a,b,c)
  return sonlar
#ustozning javoblari
def kattasi(x,y,z):
    max = x
    if y>=max:
        max = y
    if z>=max:
        max = z
    return max

kattasi(10,20,-5)
#4
def aylana_info(radiusi):
  """Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya"""
  malumotlar = {'radius':radiusi,
                'diametr':2*radiusi,
                'perimetr':2*3.14*radiusi,
                'yuz':2*radiusi**2}
#5
def tubson_top(x,y):
    """Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya""" 
    tubsonlar=[]  
    for i in range(x, y + 1):
        ishora = False
        if i < 2:
            continue
        if i == 2:
            tubsonlar.append(2)
            continue
        for x in range(2, i):
            if i % x == 0:
                ishora = True
                break
        if ishora == False:
            tubsonlar.append(i)    
    return tubsonlar
#ustozning javoblari
def tub_sonlar_top(min,max):    
    tub_sonlar = []    
    for n in range(min,max+1):
        tub = True
        if (n==1):
            tub = False
        elif(n==2):
            tub = True
        else:
            for x in range(2,n):
                if(n%x==0):
                    tub = False
        if tub:
            tub_sonlar.append(n)
                
    return tub_sonlar
#6
def PrintFibonacci(uzunlik):
    bir = 0
    ikki = 1
    print(bir, ikki, end=" ")
    uzunlik -= 2
    while uzunlik > 0:
        print(bir + ikki, end=" ")   
        temp = ikki
        ikki = bir + ikki
        bir = temp       
        uzunlik -= 1             
#ustozning javoblari
def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)        
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar

print(fibonacci(10))
