# talaba_0 = {
#     "ism": "Muslihiddin",   
#     "familiya": "Nurmamatov",
#     "yosh": 17,
# }

# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat}\n")







# telefonlar = {
#     "ali": "iphone x",
#     "vali": "galaxy s20",
#     "olim": "mi 10 pro",
#     "orif": "nokia 9",
# }

# for ism, model in telefonlar.items():
#     print(f"{ism.title()}ning telefoni: {model}")







# mahsulotlar = {
#     "olma": 5000,
#     "banan": 7000,                                         # sorted - kalitlarni tartiblab beradi
#     "shaftoli": 8000,
#     "nok": 6000,
#     "uzum": 9000
#     }
# for meva in mahsulotlar.keys():       # yoki print(mahsulotlar.keys())
#     print(meva.title())
    
    
# bozorlik = ["uzum", "nok", "qovun", "anor", "olma"]
# for mahsulot in bozorlik:
#     if mahsulot in mahsulotlar.keys():
#         print(f"{mahsulot.title()} do'konimizda bor. Narxi {mahsulotlar[mahsulot]} so'm.")
#     else:
#         print(f"{mahsulot.title()} do'konimizda yo'q.")








#set funktsiyasi yordamida lug'atdagi takroriy qiymatlarni olib tashlash mumkin
# telefonlar = {
#     "ali": "iphone x",
#     "vali": "galaxy s20",
#     "olim": "mi 10 pro",
#     "orif": "nokia 9",
#     "hamro": "iphone x",
#    "nematulloh": "nokia 9"
#    }                                                              # values() - faqat qiymatlarni oladi ya'ni kalitlarni emas
# for model in set(telefonlar.values()):                            # yoki print(set(telefonlar.values()))
#     print(model)
    








# set - funktsiyasi yordamida lug'atdagi takroriy qiymatlarni olib tashlash mumkin
# masalan:
# telefonlar = {"ball", "nokia", "samsung", "nokia", "iphone", "samsung"}
# for telefon in set(telefonlar):
#     print(telefon)











