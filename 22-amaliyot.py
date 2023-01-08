#1
def kopaytir(*sonlar):
  """Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya"""
  kopaytma = 1
  for son in sonlar:
    kopaytma *= son
  return kopaytma
kopaytir(25,455)
#2
def talaba_info(ism,familiya,**malumotlar):
  malumotlar['ism']=ism
  malumotlar['familiya']=familiya
  return malumotlar
talaba_info("Barkamol","O`rinboyev",yil=2003)
