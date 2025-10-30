# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <10:
#     print("Sizga kirish bepul!")
# elif yosh <=20:
#     print("Sizga kirish 10 000 so'm.")
# else:
#     print("Sizga kirish 50 000 so'm.")









# kun = input("Bugun hafta kuni nima? ")
# if kun.lower() == "shanba" or kun.lower() == "yakshanba":
#     print("Bugun dam olish kuni!")
# elif kun.lower() == "dushanba" or kun.lower() == "seshanba" or kun.lower() == "chorshanba" or kun.lower() == "payshanba" or kun.lower() == "juma":
#     print("Bugun ish kuni!")
# else:
#     print("Bunday kun yoq!")











# kun = input("Bugun qaysi kun? ")
# harorat = float(input("Havo harorati qanday? "))

# if kun.lower() == "yakshanba" and harorat >=30:
#     print("Bugun dam olish kuni va havo issiq, cho'milgani boramiz!")
# elif kun.lower() == "yakshanba" and harorat <30:
#     print("Bugun dam olish kuni, lekin havo issiq emas, uyda dam olamiz.")
# else:
#     kun.lower() == "dushanba" or kun == "seshanba" or kun == "chorshanba" or kun == "payshanba" or kun == "juma"
#     print("Bugun ish kuni, ishga boramiz.")








# ovqat = 15000
# choy = True
# salat = False
# if choy and salat:
#     narh = ovqat + 10000
# elif choy or salat:
#     narh = ovqat + 5000
    
# print(f"Jami narh: {narh} so'm")









# narh = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False

# if choy:
#     print("Choy oldingiz.")
#     narh = narh + 3000
# elif not choy:
#     print("Choy olmadingiz.")
    
# if salat:
#     print("Salat oldingiz.")
#     narh = narh + 5000
# elif not salat:
#     print("Salat olmadingiz.")
    
# if non:
#     print("Non oldingiz.")
#     narh = narh + 2000
# elif not non:
#     print("Non olmadingiz.")
    
# if kompot:
#     print("Kompot oldingiz.")
#     narh = narh + 5000
# elif not kompot:
#     print("Kompot olmadingiz.")
    
# if assorti:
#     print("Assorti oldingiz.")
#     narh = narh + 15000
# elif not assorti:
#     print("Assorti olmadingiz.")
    
# print(f"Jami narh: {narh} so'm")















#                           01
# menu = ["osh", "qazonkabob", "shashlik", "lag'mon", "somsa"]
# ovqat = input("Nima ovqat yeysiz? ")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi.")
# else:
#     print("Afsuski, bizda bunday ovqat yo'q.")
    
#                           02
# menu = ["osh", "qazonkabob", "shashlik", "lag'mon", "somsa"]
# ovqat = input("Nima ovqat yeysiz? ")
# if ovqat.lower() not in menu:
#     print("Afsuski, bizda bunday ovqat yo'q.")
# else:
#     print("Buyurtma qabul qilindi.")
    
    
    
    
    
    
    
    
    
    
menu = ["osh", "qazonkabob", "shashlik", "lag'mon", "somsa"]
buyurtmalar = ["osh", "shashlik", "manti", "lag'mon", "beshbarmak"]
if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor.")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q.")
            
else:
    print("Siz hech narsa buyurtma qilmagansiz.")