# BMI Calculator
`BMI(body mass index) - TMI(tana massasi indeksi)`

Yozuvchi: Barkamol Urinboev

ism = input("Ismingizni kiriting:")
ogirlik = int(input("Og`irligingizni kilogramda kiriting: "))
balandlik = float(input("Balandligingini  metrda kiriting: "))

TMI =  ogirlik / (balandlik * balandlik)
print(TMI)

if TMI>0:
    if(TMI<18.5):
        print(f"{ism}, sizda vazn yetishmovchiligi!")
    elif(TMI<=24.9):
        print(f"{ism}, sizning vazningiz mo`tadil!")
    elif(TMI<29.9):
        print(f"{ism}, sizda ozroq ortiqcha vazn bor, Harakatni ko`paytiring!")
    elif(TMI<34.9):
        print(f"{ism}, sizda ko`p ortiqcha vazn bor, Shifokorga ko`rinishni unutmang!")
    else:
        print(f"{ism}, sizda o`ta ko`p ortiqcha vazn bor, Zudlik bilan shifokorga ko`rining!")
else: 
    print("To`g`ri qiymat kiriting")
