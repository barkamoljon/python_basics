#1
imom_buxoriy = {'ism':'imom muhammad ibn ismoil buxoriy','t_yil':810,'m_asarlar':['Sahihul Buxoriy','Tarixul Kabir','Tarixul Sag`ir']}
imom_gazzoliy = {'ism':'imom abu homid g`azzoliy','t_yil':1058,'m_asarlar':['Ihyayu ulumud din','Mukoshafut-ul Qulub','Kimyo-i Saodat']}
imom_termiziy = {'ism':'imom muhammad ibn iso termiziy','t_yil':824,'m_asarlar':['Sunani Termiziy','Shamoilu Mahammadiy','At-Tarix','Az-Zuhd']}
imom_navaviy = {'ism':'imom yahyo ibn sharaf navaviy','t_yil':1233,'m_asarlar':['Riyozus-Solihin','Al-Arbaʿīn al-navaviy','Al-Adkor']}
shaxslar = [imom_buxoriy,imom_gazzoliy,imom_termiziy,imom_navaviy]            
for shaxs in shaxslar:
      print(f"Hazrat {shaxs['ism'].title()}, "
            f"{shaxs['t_yil']}-yili tug`ilganlar, ")
          
#2
for shaxs in shaxslar:
  ism =shaxs['ism']
  asarlar = shaxs['m_asarlar']
  print(f"\nHazrat {ism} ning eng mashhur asarlari:")
  for asar in asarlar:
    print(asar)
#3
kinolar = {
    'abdulloh':['transformers','transformers 2','transformers 3'],
    'abdurahman':['forsaj','forsaj 2','forsaj 3'],
    'abdusomad':['avangers','avangers 2', 'avangers 3']
}
for ism,films in kinolar.items():
   print(f"\n{ism.title()} quyidagi kinolarni yaxshi ko`radi: ")
   for film in films:
     print(f'{film.capitalize()}')
#4
davlatlar ={
        "o`zbekiston":{'yer_maydoni':447_400 ,
           'aholi':35,
           'til':'o`zbek'
           },
    "aqsh":{'yer_maydoni':9_826_630 ,
           'aholi':331,
           'til':'ingliz'},
    'misr':{'yer_maydoni':1_001_450,
           'aholi':101,
           'til':'arab'},
    }
for davlat, info  in davlatlar.items():
  if davlat.lower()=='aqsh':
    davlat = davlat.upper()
  else:
    davlat = davlat.capitalize()
  print(f"\n {davlat} yer maydoni {info['yer_maydoni']} km, "
        f"aholisi {info['aholi']}mln kishi,tili {info['til']}")
#5 mening javobim
davlat = input("Istalgan davlat nomini kiriting: ").lower()
davlat_ = davlatlar.get(davlat)
if davlat_== None:
  print("Bizda bunday ma'lumot yo'q")
else:
  if davlat.lower()== 'aqsh':
    davlat = davlat.upper()
  else: 
    davlat = davlat.capitalize()
  print(f"{davlat}:aholisi {davlat_['aholi']} million,",
        f"yer maydoni {davlat_['yer_maydoni']}km kvadrat, asosiy til {davlat_['til']} tili.")
#5 Ustozning javoblari
davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }

davlat = input('Davlat nomini kiriting: ').lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")
