# input()                                                   # foydalanuvchidan ma'lumot olish uchun ishlatiladi

# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = int(input(savol))
# height = float(input("Bo'yingiz necha metr? "))






# while()                
# son = 1
# while son <= 5:
#     print(son, end=' ')
#     son += 1               # son = son + 1






#   input() va while() 

# print("Sonni kvadratini qaytaruvchi dastur.")
# savol = "Istalgan sonni kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(f"{qiymat} ning kvadrati {int(qiymat)**2} ga teng.")
# print("Dastur tugadi.")









# ishora

# print("Sonni kvadratini qaytaruvchi dastur.")
# savol = "Istalgan sonni kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(f"{qiymat} ning kvadrati {int(qiymat)**2} ga teng.")








# break buyrug'i

# print("Sonni kvadratini qaytaruvchi dastur.")
# savol = "Istalgan sonni kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(f"{qiymat} ning kvadrati {int(qiymat)**2} ga teng.")
















# break va for 

# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng.")








# continue buyrug'i

# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng.")


















# continue va while

# son = 0
# while son < 10:
#     son += 1
#     if son % 2 == 0:
#         continue
#     print(son)









#infinite loop - cheksiz sikl  

son = 0
while son < 10:
    if son % 2 == 0:                                               # cheksiz siklni to'xtatish uchun son qiymatini oshirish kerak
        continue                                                   # ya'ni son += 1 qo'shish kerak
    print(son)