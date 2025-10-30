# mehmonlar = ["Ali", "Vali", "Hasan", "Husan"]
# for mehmon in mehmonlar:
#     print("Salom, " + mehmon)


    
# mehmonlar = ["Ali", "Vali", "Hasan", "Husan"]
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20-dekabr kuni soat 20:00 da bo'lib o'tadigan tadbirga taklif qilamiz.")
#     print("Hurmat bilan, Muslihiddin Nurmamatov.\n")



# sonlar = list(range(1, 11))                             # 1 dan 10 gacha bo'lgan sonlar ro'yxatini yaratish
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")      # har bir sonning kvadratini chiqarish




# sonlar = list(range(11))                                  # 0 dan 10 gacha bo'lgan sonlar ro'yxatini yaratish
# sonlar_kvadrati = []                                      # bo'sh ro'yxat yaratish
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)                        # har bir sonning kvadratini ro'yxatga qo'shish
# print(sonlar)                                             
# print(sonlar_kvadrati)                                    





dostlar = []
for n in range(5):
    dostlar.append(input(f"{n+1}-dostingizning ismini kiriting: "))
print("Dostlaringiz ro'yxati:", dostlar)