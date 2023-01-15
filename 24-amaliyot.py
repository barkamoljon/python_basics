#1
lambda x:x*10
javob = lambda x:x*10
print(javob(10))
#2
lambda x,y:x+y
javob2 = lambda x,y:x+y
print(javob2(2,45))
#3
import random as r
#lambda x:x**2,sonlar
a = list(range(100))
sonlar = r.sample(a,10)
print(sonlar)
javob3 = list(map(lambda x:x**2,sonlar))
print(javob3)
#4
lambda x:x%2!=0,sonlar
javob4 = list(filter(lambda x:x%2!=0,sonlar))
print(javob4)
#5
def isPrime(n):
  
    # Corner case
    if n <= 1:
        return False
  
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False;
  
    return True
tub_sonlar2 = list(filter(isPrime,range(100)))

#ustoz yechimlari
def tubmi(x):
    if x % 2 == 0 or x < 2:
        return False  # Son juft yoki 2 dan kichik bo'lsa
    if x == 2 or x == 3:
        return True  # Son 2 yoki 3 bo'lsa
    for i in range(3, x, 2):
        if x % i == 0:
            return False
    return True


tub_sonlar = list(filter(tubmi, range(100)))
print(tub_sonlar)
