# import math

# uzunlik = lambda pi, r : 2 * pi * r
# print(uzunlik(math.pi, 10))




# kvvadrat = lambda x,y : x ** y
# print(kvvadrat(5, 2)) 





# def daraja(n):
#     return lambda x : x ** n

# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"5 ning kvadrati: {kvadrat(5)},\n5 ning kubi: {kub(5)} ga teng") 















# from math import sqrt

# sonlar = list(range(1,11))
# ildizlar = list(map(sqrt,sonlar))
# print(ildizlar)






# sonlar = list(range(1,11))
# kvadratlar = list(map(lambda x:x*x,sonlar)) 
# # print(kvadratlar)

# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
# sonlar = list(map(lambda x,y:x+y,a,b))
# print(sonlar)





import random as r

# sonlar = r.sample(range(100), 10)                                              # sample - tasodifiy sonlarni chiqarib beradi
# print(sonlar)

# def juftmi(x):
#     """x juft bo'lsa True, toq bo'lsa False qaytaruvchi funksiya"""
#     return x%2 == 0

# # juft_sonlar = list(filter(juftmi, sonlar))                                     # filter - saralovchi funksiya
# # print(juft_sonlar)

# juft_sonlar = list(filter(lambda x: x%2 == 0,))







mevalar = ['olma', 'anor', 'shaftoli', 'nok', 'uzum', 'mandarin', 'qovun', 'banan']
harf = "o"
mevalar_b = list(filter(lambda meva: meva.startswith(harf), mevalar))                # startswith - stringdan boshlanishini tekshiruvchi funksiya ya'ni harf bilan boshlanadigan mevalar ro'yxatini qaytaradi
# print(mevalar)
mevalar2 = list(filter(lambda meva: len(meva) <=5, mevalar))
# print(mevalar2)

a = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))
print(a)