# car0 = {
#     "model": "cobalt",
#     "rang": "oq",
#     "yil": 2020,
#     "narh": 13000,
#     "km": 5000,
#     "karobka": "avtomat",
# }

# car1 = {
#     "model": "nexia 3",
#     "rang": "qora",
#     "yil": 2019,
#     "narh": 9000,
#     "km": 20000,
#     "karobka": "mexanika",
# }

# car2 = {
#     "model": "gentra",
#     "rang": "qizil",
#     "yil": 2021,
#     "narh": 11000,
#     "km": 10000,
#     "karobka": "avtomat",
# }

# cars = [car0, car1, car2]
# for car in cars:
#     print(
#         f"{car['model'].title()}, "
#         f"{car['rang']} rang, "
#         f"{car['yil']}-yil, "
#         f"{car['km']} km, "
#         f"{car['narh']}$, "
#         f"{car['karobka']} karobka"
#     )

# print(f"{cars[2]['rang'].title()} "
#       f"{cars[2]['model']}")


















# malibus = []
# for n in range(10):
#     new_car = {
#         "model": "malibu",
#         "rang": None,
#         "yil": 2020,
#         "narh": None,
#         "km": 0,
#         "karobka": "avtomat",
#     }
#     malibus.append(new_car)
    
    
# for malibu in malibus[:3]:
#     malibu["rang"] = "qora"

# for malibu in malibus[3:6]:
#     malibu["rang"] = "oq"
    
# for malibu in malibus[6:]:
#     malibu["rang"] = "qizil"
#     malibu["karobka"] = "mexanika"
    
# for malibu in malibus:
#     if malibu["karobka"] == "avtomat":
#         malibu["narh"] = 40000
#     else:
#         malibu["narh"] = 35000
    
# print(malibu)
# print(malibus)















# LUGAT ICHIDA RO'YXAT

# dasturchilar = {
#     "ali": ["python", "c++"],   
#     "vali": ["java", "c#","ruby"],
#     "hasan": ["html", "css", "js"],
#     "husan": ["php", "sql"],
# }

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(f"{til.upper()}")





# LUGAT ICHIDA LUG'AT

hamkasblar = {
    "ali": {
        "familiya": "valiyev",
        "yosh": 25,
        "malumot": "oliy",
        "tillar": ["python", "c++"],
    },
    "vali": {
        "familiya": "aliyev",
        "yosh": 30,
        "malumot": "o'rta-maxsus",
        "tillar": ["html", "css", "js"],
    },
    "hasan": {
        "familiya": "husanov",
        "yosh": 28,
        "malumot": "maxsus",
        "tillar": ["php", "sql"],
    },
}

for ism, info in hamkasblar.items():                               # items - kalit va qiymatni olib beradi
    print(f"\n{ism.title()} {info['familiya'].title()}:")          # info - lug'at
    print(f"Yoshi: {info['yosh']}")
    print(f"Ma'lumoti: {info['malumot']}")
    print("Dasturlash tillari:")
    for til in info['tillar']:
        print(f"{til.upper()}")