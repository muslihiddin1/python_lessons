# cars = ["BMW", "Audi", "Toyota", "Mercedes", "Honda", "Kia", "Hyundai", "Mazda", "Nissan", "Volkswagen"]
# cars.sort(reverse=True)                                # Avtomobillar ro'yxatini teskari alifbo tartibida saralash
# cars.sort()                                            # Avtomobillar ro'yxatini alifbo tartibida saralash
# cars.sorted()                                          # Avtomobillar ro'yxatini alifbo tartibida vaqtincha saralash
# print(sorted(cars, reverse = True))                    # Avtomobillar ro'yxatini teskari alifbo tartibida vaqtincha saralash




# summa = [12000, 15000, 18000, 20000, 25000]
# arzon = min(summa)                                     # eng arzon narx
# qimmat = max(summa)                                    # eng qimmat narx
# jami = sum(summa)                                      # narxlar yig'indisi
# print("Eng arzon narx:", arzon, ".Eng qimmat narx:", qimmat, ".Jami narxlar:", jami)


# summa = cars[:]                                        # ro'yxat nusxasi


# my_cars = ["BMW", "Audi", "Toyota", "Mercedes"]
# print(my_cars)
# print(my_cars[2:5])                                    # 2-indeksdan 5-indeksgacha bo'lgan elementlar
# print(my_cars[:4])                                     # 0-indekstdan 4-indeksgacha bo'lgan elementlar
# print(my_cars[1:])                                     # 1-indeksdan oxirigacha bo'lgan elementlar
# print(my_cars[-3:])                                    # oxirgi 3 ta element


taomlar = ["osh", "qazonkabob", "shashlik", "lag'mon", "somsa"]
nonushta = taomlar[:]                                   # taomlar ro'yxatining nusxasini yaratish
nonushta.append("qaymoq")                               # nonushta ro'yxatiga yangi taom qo'shish
nonushta.append("choy")                                 # nonushta ro'yxatiga yangi taom qo'shish
print("Taomlar ro'yxati:", taomlar)
print("Nonushta ro'yxati:", nonushta)