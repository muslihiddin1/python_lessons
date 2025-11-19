# *args yordamida moslashuvchan sonli argumentlarni qabul qilish
# **kwargs yordamida kalit so'z argumentlarini qabul qilish


# def summa(*sonlar):
#     """Berilgan sonlarning yig'indisini hisoblaydigan funksiya."""
#     jami = 0
#     for son in sonlar:
#         jami += son
#     return jami

# print(summa(1, 2, 3))          # 6
# print(summa(10, 20, 30, 40))   # 100
# print(summa())                 # 0

#yoki

# def summa(*sonlar):
#     """Berilgan sonlarning yig'indisini hisoblaydigan funksiya."""
#     return sum(sonlar)

# print(summa(1, 2, 3))          # 6
# print(summa(10, 20, 30, 40))   # 100
# print(summa())                 # 0














# def summa(x,y, *sonlar):
#     """Berilgan sonlarning yig'indisini hisoblaydigan funksiya."""
#     return x + y + sum(sonlar)

# print(summa(1, 2, 3))          # 6
# print(summa(10, 20, 30, 40))   # 100
# print(summa(5, ))              # 5           #x va y ni berish shart bu yerda 1 ta bo'lgani uchun xatolik beradi,
#                                              #kamida 2 ta qiymat berish kerak x va y uchun







# **kwargs misol


# def avto_info(kompaniya, model, **malumotlar):
#     """Avtomobil haqida ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya."""
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar
# avto1 = avto_info('GM', 'Malibu', rang='qora', yil=2018,)                      # malumot kirgizmoqchi bo'lsa kalit so'z va qiymat ko'rinishida kiritish kerak
# avto2 = avto_info('Toyota', 'Camry', rang='oq', yil=2020, narh=40000)
# print(avto1)
# print(avto2)


















# AMALIYOT
# 01. Berilgan sonlarning ko'paytmasini hisoblaydigan funksiya yozing.
def multiply(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma

print(multiply(4,5,6))








# 02. Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. 
# Talabaning ismi va familiyasi majburiy argument, 
# qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

def talaba(ism, familiya, **malumotlar):
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar
talaba1 = talaba('ali', 'valiyev', yosh=20, kurs=3, fakultet='matematika')
talaba2 = talaba('hasan', 'husanov', yosh=22, kurs=4)
print(talaba1)
print(talaba2)