# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# ismlar = []
# n = 1   
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (yes/no): ")
#     n+=1
#     if javob.lower() != 'yes':
#         break
    
# print("\nSizning do'stlaringiz ro'yxatingiz:")
# for ism in ismlar:
#     print(ism.title())  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# print("Do'stlaringiz yoshini saqlaymiz.")
# yoshlar = {}
# ishora = True
# while ishora:
#     ism = input("\nDo'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     yoshlar[ism] = int(yosh)
#     javob = input("Yana ma'lumot qo'shasizmi? (yes/no): ")
#     if javob.lower() != 'yes':
#         ishora = False
        
# print("\nDo'stlaringiz yoshlari ro'yxati:")
# for ism, yosh in yoshlar.items():
#     print(f"{ism.title()}ning yoshi {yosh} da.")




















# cars = ["lacetti", "nexia", "gentra", "malibu", "nexia", "damas", "nexia"]
# while "nexia" in cars:
#     cars.remove("nexia")
# print(cars)












# talabalar = ["ali", "vali", "hasan", "husan"]
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi.")
#     baholangan_talabalar[talaba] = int(baho)


















# homework

savat = []
while True:
    mahsulot = input("Savatga mahsulot qo'shing:")
    savat.append(mahsulot)
    javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
    if javob != "ha":
        break
print("Dastur tugadi!")

mahsulotlar = {}
while True:
    mahsulot = input("Mahsulot nomini kiriting: ")
    narh = input(f"{mahsulot.title()}ning narhini kiriting: ")
    mahsulotlar[mahsulot] = narh
    javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
    if javob != "ha":
        break
print("Mahsulotlar qo'shildi")

buyurtmalar = ["olma", "anjir", "uzum", "qovun"]
mahsulotlar = {"olma": 20000, "shaftoli": 25000, "tarvuz": 18000, "uzum": 22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")