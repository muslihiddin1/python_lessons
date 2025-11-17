# def toliq_ism_yasa(ism, familiya):
#     """Foydalanuvchining to'liq ismini qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism                                                        # return - qiymat qaytaradi --- bundan keyinchalik foydalanish mumkin bo'ladi
    
# talaba1 = toliq_ism_yasa("Muslihiddin", "Nurmamatov")
# talaba2 = toliq_ism_yasa("Ne'matullo", "Nurmamatov")
# print(f"Talaba 1: {talaba1.title()}")
# print(f"Talaba 2: {talaba2.title()}")













# def avto_info(model, rang, yil, narh=None):
#     """Avtomobil haqida ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     avto = {
#         "model": model,
#         "rang": rang,
#         "yil": yil,
#         "narh": narh,
#     }
#     return avto
# avto1 = avto_info("Gentra", "qora", 2020,)
# avto2 = avto_info("Malibu", "oq", 2021, 20000)
# avtolar = [avto1, avto2]
# for avto in avtolar:
#     if avto["narh"]:
#         narh = avto["narh"]
#     else:
#         narh = "Noma'lum"
#     print(f"{avto["rang"]}, {avto["model"]}. Narhi: {narh}")











# def oraliq(min, max):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# print(oraliq(1, 10))  
# print(oraliq(10, 21))














# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {
#         "kompaniya": kompaniya,
#         "model": model,
#         "rang": rangi,
#         "korobka": korobka,
#         "yil": yili,
#         "narh": narhi,
#     }
#     return avto


# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar = []  # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting", end="")
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rangi = input("Rangi: ")
#     korobka = input("Korobka: ")
#     yili = input("Ishlab chiqarilgan yili: ")
#     narhi = input("Narhi: ")
#     # Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida
#     # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob == "no":
#         break

# print("\nSalonimizdagi avtolar:")
# for avto in avtolar:
#     if avto["narh"]:
#         narh = avto["narh"]
#     else:
#         narh = "Noma'lum"
#     print(
#         f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. Narhi: {narh}"
#     )


















# AMALIYOT


# 01
# def mijoz_info(ism, familiya, tyil, tjoy, email="", tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz = {
#         "ism": ism,
#         "familiya": familiya,
#         "tyil": tyil,
#         "yoshi": 2025 - tyil,
#         "tjoy": tjoy,
#         "email": email,
#         "telefon": tel,
#     }
#     return mijoz


# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar = []
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob != "ha":
#         break

# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(
#         f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
#         f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}"
#     )





# 02
