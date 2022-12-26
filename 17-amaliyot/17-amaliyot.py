#1
kitob_sora = ("Yaxshi ko`rgan kitobning nomini kiriting: ")
kitob_sora += "(dasturni to`xtatish uchun 'stop'ni bosing): "
qiymat = ''
while qiymat != 'stop':
    qiymat = input(kitob_sora)
#2
savol = "Yoshingizni kiriting "
savol += "(dasturni to'xtatish uchun 'exit' yoki 'quit deb yozing): "
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit'or qiymat=='quit':
        ishora = False
    else:
      qiymat = int(qiymat)
      if qiymat<7:
        print("Sizga kirish 2000 so`m")
      elif qiymat<18:
        print("Sizga kirish 3000 so`m")
      elif qiymat>65:
        print("Sizga kirish bepul")
      elif qiymat>=18:
        print("Sizga kirish 10000 so`m")
#2.2)
savol = "Yoshingizni kiriting "
savol += "(dasturni to'xtatish uchun 'exit' yoki 'quit deb yozing): "
qiymat = ''
while True:
    qiymat = input(savol)
    if qiymat == 'exit'or qiymat=='quit':
      break
    else: 
      qiymat = int(qiymat)
      if qiymat<7:
        print("Sizga kirish 2000 so`m")
      elif qiymat<18:
        print("Sizga kirish 3000 so`m")
      elif qiymat>65:
        print("Sizga kirish bepul")
      elif qiymat>=18:
        print("Sizga kirish 10000 so`m")
#Shunday qilish ham mumkin
#2.3)
savol = "Yoshingizni kiriting "
savol += "(dasturni to'xtatish uchun 'exit' yoki 'quit deb yozing): "
qiymat = ''
while qiymat != 'exit'or qiymat!='quit':
    qiymat = input(savol)
    if qiymat == 'exit'or qiymat=='quit':
      break
    else: 
      qiymat = int(qiymat)
      if qiymat<7:
        print("Sizga kirish 2000 so`m")
      elif qiymat<18:
        print("Sizga kirish 3000 so`m")
      elif qiymat>65:
        print("Sizga kirish bepul")
      elif qiymat>=18:
        print("Sizga kirish 10000 so`m")
#Ustozning javoblari, yechimda farq yo`q shunchaki boshqa uo`l bilan ishlangan
savol = "Yoshingizni kiriting: "

while True:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'quit':
        break
    yosh = int(qiymat)
    
    if yosh<7:
        narh = 2000
    elif 7<=yosh<18:
        narh = 3000
    elif 18<=yosh<65:
        narh = 10000
    else: narh = 0
    
    if narh==0:
        print("Sizga chipta bepul")
    else:
        print(f"Chipta {narh} so'm")
#3
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
qiymat = ''
while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        print("Musbat son kiritmadingiz!")
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
#Ustozning javoblari to`g`riroq
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
