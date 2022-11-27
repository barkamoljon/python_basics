#1
ismlar = ['Alisher', 'Abdulloh', 'Sardor']
#2
print(f"Assalomu Alaykum {ismlar[0]}")
print(f"Assalomu Alaykum va Rohmatulloh {ismlar[1]}")
print(f"Assalomu Alaykum va Rohmatulloh va Barokatuh {ismlar[2]}")
#3
sonlar = [1, -3, 2.3, 5]
#4
print(sonlar[0] + sonlar[1])
print(sonlar[0] / sonlar[3])
print(sonlar[0] * sonlar[2])
sonlar[2] = 3
sonlar[0] = 5
sonlar[3] = 1
print(sonlar)
#5
t_shaxslar = ['Imom Buxoriy', 'Imom Navaviy','Imom G`azzoliy']
z_shaxslar = ['Ilon Mask', 'Bill Geyts', 'Shayx Muhammad Sodiq Muhammad Yusuf']
print(f"""Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan,
zamonaviy shaxslardan esa {z_shaxslar.pop(1)} bilan 
suhbat qilishni istar edim""")
#6
friends = []
friends.append('Abdulloh')
friends.append('Abbos')
friends.append('Ali')
friends.append('Abdulaziz')
friends.append('Abdulhamid')
#7
friends.remove('Abdulloh')
friends.remove('Abdulhamid')
#8
friends.insert(0,'Mas\'ud')
friends.insert(2,'Ja`far')
friends.insert(4,'Ubay')
print(friends)
#9
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(2))
print('\nKelgan mehmonlar: ',mehmonlar)
