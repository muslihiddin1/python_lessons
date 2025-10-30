# car_0 = {"model": "lacetti", "rang": "oq", "yil": 2018, "narh": 13000}
# print(car_0["model"])
# print(car_0["rang"])








# en_uz = {
#     "apple": "anor",
#     "banana": "banan",
#     "peach": "shaftoli",
#     "pear": "nok",  
#     "grape": "uzum"
# }
# print("apple so'zining o'zbekcha tarjimasi:", en_uz["apple"])
# en_uz["orange"] = "apelsin"                                                   # yangi juftlik qo'shish
# en_uz["apple"] = "olma"                                                        # mavjud kalitni o'zgartirish
# print(en_uz)












# mevalar = {
#     "olma": 5000,
#     "banan": 7000,
#     "shaftoli": 8000,
#     "nok": 6000,
#     "uzum": 9000
#     }
# print(f"Olma narxi: {mevalar['olma']} so'm")
# print(f"Nok narxi: {mevalar['nok']} so'm")
# print(f"Uzum narxi: {mevalar['uzum']} so'm")
# print(f"Banan narxi: {mevalar['banan']} so'm")
# print(f"Shaftoli narxi: {mevalar['shaftoli']} so'm")












# talaba_0 = {
#     "ism": "Muslihiddin",
#     "familiya": "Nurmamatov",
#     "yosh": 17,
# }
# print(f"{talaba_0['ism'].title()} \
#     {talaba_0['familiya'].title()},\
#     {talaba_0['yosh']} yoshda")







# # # Bo'sh lug'at yaratish
# talaba_1 = {} 
# talaba_1["ism"] = "Muslihiddin"
# talaba_1["familiya"] = "Nurmamatov"
# talaba_1["yosh"] = 17
# print(talaba_1)
# print(f"{talaba_1['ism'].title()} \
#     {talaba_1['familiya'].title()},\
#     {talaba_1['yosh']} yoshda") 









# # # # kalit so'zni o'chirish'
# talaba_0 = {
#     "ism": "Muslihiddin",
#     "familiya": "Nurmamatov",
#     "yosh": 17,
# }
# del talaba_0["yosh"]  # 'yosh' kalit so'zini o'chirish
# print(talaba_0)







#get metodi
# talaba_0 = {
#     "ism": "Muslihiddin",
#     "familiya": "Nurmamatov",
#     "yosh": 17,
# }
# print(talaba_0.get("ism"))                                            # mavjud kalit so'z
# print(talaba_0.get("kurs"))                                           # mavjud bo'lmagan kalit so'z
# print(talaba_0.get("kurs", "Bunday kalit so'z mavjud emas"))          # mavjud bo'lmagan kalit so'z uchun xabar chiqarish